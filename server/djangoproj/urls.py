"""djangoproj URL Configuration."""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    # Django Admin
    path(
        'admin/',
        admin.site.urls
    ),

    # Django application API routes
    path(
        'djangoapp/',
        include('djangoapp.urls')
    ),

    # Home page
    path(
        '',
        TemplateView.as_view(
            template_name="Home.html"
        )
    ),

    # About page
    path(
        'about/',
        TemplateView.as_view(
            template_name="About.html"
        )
    ),

    # Contact page
    path(
        'contact/',
        TemplateView.as_view(
            template_name="Contact.html"
        )
    ),

    # Login React page
    path(
        'login/',
        TemplateView.as_view(
            template_name="index.html"
        )
    ),

    # Registration React page
    path(
        'register/',
        TemplateView.as_view(
            template_name="index.html"
        )
    ),

    # All dealerships React page
    path(
        'dealers/',
        TemplateView.as_view(
            template_name="index.html"
        )
    ),

    # Dealer details and reviews React page
    path(
        'dealer/<int:dealer_id>',
        TemplateView.as_view(
            template_name="index.html"
        )
    ),

    # Post-review React page
    path(
        'postreview/<int:dealer_id>',
        TemplateView.as_view(
            template_name="index.html"
        )
    ),

] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)