from django.urls import path
from .views import JobCreate, JobList, JobUpdate, JobDelete, JobDetail


app_name = 'jobs'

urlpatterns = [
    path('', JobList.as_view(), name='list_jobs'),
    path('create/', JobCreate.as_view(), name='create_job'),
    path('<slug:slug>/update', JobUpdate.as_view(), name='update_job'),
    path('<slug:slug>/delete', JobDelete.as_view(), name='delete_job'),
    path('<slug:slug>', JobDetail.as_view(), name='detail_job')
]
