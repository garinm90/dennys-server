from django.urls import path
from .views import CustomerCreate, CustomerList, CustomerUpdate, \
    CustomerDelete, CustomerDetail, CustomerUpdateRide, CustomerRideList

app_name = 'customers'

urlpatterns = [
    path('', CustomerList.as_view(), name='list_customers'),
    path('create/', CustomerCreate.as_view(), name='create_customer'),
    path('<int:pk>/update', CustomerUpdate.as_view(), name='update_customer'),
    path('<int:pk>/delete', CustomerDelete.as_view(), name='delete_customer'),
    path('<int:pk>/', CustomerDetail.as_view(), name='detail_customer'),
    path('<int:pk>/add_rides', CustomerUpdateRide.as_view(),
         name='rides_customer'),
    path('<int:pk>/rides', CustomerRideList.as_view(),
         name='list_customer_rides')
]
