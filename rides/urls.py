from django.urls import path
from .views import RideCreate, RideList, RideUpdate, RideDelete

urlpatterns = [
    path('', RideList.as_view(), name='list_ride'),
    path('create/', RideCreate.as_view(), name='create_ride'),
    path('<int:pk>/update', RideUpdate.as_view(), name='update_ride'),
    path('<int:pk>/delete', RideDelete.as_view(), name='delete_ride')
]
