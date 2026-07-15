from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import CarMake, CarModel
from .populate import initiate
from .restapis import (
    get_request,
    analyze_review_sentiments,
    post_review
)

import logging
import json


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Login view
@csrf_exempt
def login_user(request):

    data = json.loads(request.body)

    username = data['userName']
    password = data['password']

    user = authenticate(
        username=username,
        password=password
    )

    response_data = {
        "userName": username
    }

    if user is not None:

        login(request, user)

        response_data = {
            "userName": username,
            "status": "Authenticated"
        }

    return JsonResponse(response_data)


# Logout view
def logout_request(request):

    logout(request)

    data = {
        "userName": ""
    }

    return JsonResponse(data)


# Registration view
@csrf_exempt
def registration(request):

    data = json.loads(request.body)

    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']

    if User.objects.filter(
        username=username
    ).exists():

        return JsonResponse({
            "userName": username,
            "error": "Already Registered"
        })

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name
    )

    login(request, user)

    return JsonResponse({
        "userName": username,
        "status": "Authenticated"
    })


# Get all car models and car makes
def get_cars(request):

    count = CarModel.objects.count()

    if count == 0:
        initiate()

    car_models = (
        CarModel.objects
        .select_related('car_make')
    )

    cars = []

    for car_model in car_models:

        cars.append({
            "CarModel": car_model.name,
            "CarMake": car_model.car_make.name
        })

    return JsonResponse({
        "CarModels": cars
    })


# Get all dealerships or dealerships by state
def get_dealerships(
    request,
    state="All"
):

    if state == "All":

        endpoint = "/fetchDealers"

    else:

        endpoint = (
            "/fetchDealers/"
            + state
        )

    dealerships = get_request(
        endpoint
    )

    return JsonResponse({
        "status": 200,
        "dealers": dealerships
    })


# Get the details of one dealer
def get_dealer_details(
    request,
    dealer_id
):

    endpoint = (
        "/fetchDealer/"
        + str(dealer_id)
    )

    dealer = get_request(
        endpoint
    )

    return JsonResponse({
        "status": 200,
        "dealer": dealer
    })


# Get reviews for a particular dealer
def get_dealer_reviews(
    request,
    dealer_id
):

    endpoint = (
        "/fetchReviews/dealer/"
        + str(dealer_id)
    )

    reviews = get_request(
        endpoint
    )

    # Add sentiment to every review
    if reviews is not None:

        for review_detail in reviews:

            review_text = (
                review_detail.get(
                    "review",
                    ""
                )
            )

            sentiment_response = (
                analyze_review_sentiments(
                    review_text
                )
            )

            if sentiment_response:

                review_detail["sentiment"] = (
                    sentiment_response.get(
                        "sentiment",
                        "neutral"
                    )
                )

            else:

                review_detail["sentiment"] = (
                    "neutral"
                )

    return JsonResponse({
        "status": 200,
        "reviews": reviews
    })


# Add a new dealer review
@csrf_exempt
def add_review(request):

    # Only authenticated users can post reviews
    if not request.user.is_anonymous:

        data = json.loads(
            request.body
        )

        try:

            response = post_review(
                data
            )

            return JsonResponse({
                "status": 200,
                "response": response
            })

        except Exception as error:

            logger.error(
                "Error posting review: %s",
                error
            )

            return JsonResponse({
                "status": 401,
                "message":
                    "Error in posting review"
            })

    return JsonResponse({
        "status": 403,
        "message": "Unauthorized"
    })