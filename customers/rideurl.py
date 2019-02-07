from django.urls import path
from .views import RideCreate

urlpatterns = [
    path('create/', RideCreate.as_view(), name='create_ride')
]
