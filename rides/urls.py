from django.urls import path
from . import views

app_name = 'rides'

urlpatterns = [
    path('', views.RideList.as_view(), name='list_rides'),
    path('create/', views.RideCreate.as_view(), name='create_ride'),
    path('<int:pk>/update', views.RideUpdate.as_view(), name='update_ride'),
    path('<int:pk>/delete', views.RideDelete.as_view(), name='delete_ride'),
    path('customer/<int:pk>', views.RidesCustomer.as_view(), name='customer_rides'),
]
