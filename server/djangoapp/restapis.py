import requests
import os

from dotenv import load_dotenv


# Load values from the .env file
load_dotenv()


# Backend Mongo/Node API URL
backend_url = os.getenv(
    'backend_url',
    default="http://localhost:3030"
)


# Sentiment analyzer microservice URL
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/"
)


# Send GET requests to the backend
def get_request(endpoint, **kwargs):

    params = ""

    if kwargs:

        for key, value in kwargs.items():

            params = (
                params
                + key
                + "="
                + str(value)
                + "&"
            )

    request_url = (
        backend_url
        + endpoint
        + "?"
        + params
    )

    print(
        "GET from {}".format(
            request_url
        )
    )

    try:

        # Call the backend using a GET request
        response = requests.get(
            request_url
        )

        return response.json()

    except Exception as error:

        print(
            "Network exception occurred:",
            error
        )

        return None


# Analyze the sentiment of a review
def analyze_review_sentiments(text):

    request_url = (
        sentiment_analyzer_url
        + "analyze/"
        + text
    )

    try:

        # Call the sentiment analyzer
        response = requests.get(
            request_url
        )

        return response.json()

    except Exception as error:

        print(
            f"Unexpected error={error}, "
            f"type={type(error)}"
        )

        print(
            "Network exception occurred"
        )

        return None


# Post a new review to the backend
def post_review(data_dict):

    request_url = (
        backend_url
        + "/insert_review"
    )

    try:

        # Send the review to the backend
        response = requests.post(
            request_url,
            json=data_dict
        )

        print(
            response.json()
        )

        return response.json()

    except Exception as error:

        print(
            "Network exception occurred:",
            error
        )

        return None