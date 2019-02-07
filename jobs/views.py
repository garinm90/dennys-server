from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Job
# Create your views here.


class JobList(ListView):
    model = Job
    context_object_name = 'jobs'


class JobDetail(DetailView):
    model = Job
    context_object_name = 'job'


class JobCreate(CreateView):
    model = Job
    fields = ('job_number', 'customer', 'ride',)


class JobUpdate(UpdateView):
    model = Job
    fields = ('job_number', 'customer', 'ride',)


class JobDelete(DeleteView):
    model = Job
    success_url = reverse_lazy('pages:home')
