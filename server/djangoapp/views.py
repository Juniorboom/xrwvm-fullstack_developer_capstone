from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import CarMake, CarModel
from .populate import initiate

import logging
import json


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Login view
@csrf_exempt
def login_user(request):

    # Get username and password from the request body
    data = json.loads(request.body)

    username = data['userName']
    password = data['password']

    # Authenticate the user
    user = authenticate(
        username=username,
        password=password
    )

    response_data = {
        "userName": username
    }

    # Log in if the credentials are correct
    if user is not None:

        login(request, user)

        response_data = {
            "userName": username,
            "status": "Authenticated"
        }

    return JsonResponse(response_data)


# Logout view
def logout_request(request):

    # Terminate the current user session
    logout(request)

    # Return an empty username
    data = {
        "userName": ""
    }

    return JsonResponse(data)


# Registration view
@csrf_exempt
def registration(request):

    # Read registration details from the request
    data = json.loads(request.body)

    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']

    # Check whether the username already exists
    if User.objects.filter(username=username).exists():

        return JsonResponse({
            "userName": username,
            "error": "Already Registered"
        })

    # Create the new user
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name
    )

    # Log in the newly registered user
    login(request, user)

    return JsonResponse({
        "userName": username,
        "status": "Authenticated"
    })


# Get all car models and their corresponding car makes
def get_cars(request):

    # Check whether any car models exist
    count = CarModel.objects.count()

    # Populate the database if no car models exist
    if count == 0:
        initiate()

    # Get car models with their related car makes
    car_models = CarModel.objects.select_related(
        'car_make'
    )

    cars = []

    for car_model in car_models:

        cars.append({
            "CarModel": car_model.name,
            "CarMake": car_model.car_make.name
        })

    # Return all car models as JSON
    return JsonResponse({
        "CarModels": cars
    })