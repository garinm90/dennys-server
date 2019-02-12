from django.urls import path

from .views import HomePageView, AboutPageView, RideAutocomplete

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('ride-autocomplete', RideAutocomplete.as_view(), name='ride-autocomplete'),
]
