from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = 'djangoapp'


urlpatterns = [

    # Registration route
    path(
        route='register',
        view=views.registration,
        name='register'
    ),

    # Login route
    path(
        route='login',
        view=views.login_user,
        name='login'
    ),

    # Logout route
    path(
        route='logout',
        view=views.logout_request,
        name='logout'
    ),

    # Get all car models and car makes
    path(
        route='get_cars',
        view=views.get_cars,
        name='getcars'
    ),

    # Get all dealerships
    path(
        route='get_dealers',
        view=views.get_dealerships,
        name='get_dealers'
    ),

    # Get dealerships by state
    path(
        route='get_dealers/<str:state>',
        view=views.get_dealerships,
        name='get_dealers_by_state'
    ),

    # Get details of a particular dealer
    path(
        route='dealer/<int:dealer_id>',
        view=views.get_dealer_details,
        name='dealer_details'
    ),

    # Get reviews for a particular dealer
    path(
        route='reviews/dealer/<int:dealer_id>',
        view=views.get_dealer_reviews,
        name='dealer_reviews'
    ),

    # Add a dealer review
    path(
        route='add_review',
        view=views.add_review,
        name='add_review'
    ),

] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)