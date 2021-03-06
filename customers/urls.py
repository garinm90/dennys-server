from django.urls import path
from .views import CustomerCreate, CustomerList, CustomerUpdate, \
    CustomerDelete, CustomerDetail


app_name = 'customers'

urlpatterns = [
    path('', CustomerList.as_view(), name='list_customers'),
    path('create/', CustomerCreate.as_view(), name='create_customer'),
    path('<int:pk>/update', CustomerUpdate.as_view(), name='update_customer'),
    path('<int:pk>/delete', CustomerDelete.as_view(), name='delete_customer'),
    path('<int:pk>/', CustomerDetail.as_view(), name='detail_customer'),


]
