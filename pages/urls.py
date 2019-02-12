from django.urls import path, include

from .views import HomePageView, AboutPageView, RideAutocomplete, \
    CustomerAutocomplete

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('ride-autocomplete', RideAutocomplete.as_view(),
         name='ride-autocomplete'),
    path('customer-autocomplete', CustomerAutocomplete.as_view(),
         name='customer-autocomplete'),
    path('filer/', include('filer.urls')),
]
