from django.urls import path
from .views import CustomerCreate

urlpatterns = [
    path('create/', CustomerCreate.as_view()),
]
