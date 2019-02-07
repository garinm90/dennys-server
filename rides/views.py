from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Ride


class RideList(ListView):
    model = Ride
    context_object_name = 'rides'


class RideCreate(CreateView):
    model = Ride
    fields = ('ride_name',)
    success_url = reverse_lazy('pages:home')


class RideUpdate(UpdateView):
    model = Ride
    fields = ('ride_name', )
    success_url = reverse_lazy('pages:home')


class RideDelete(DeleteView):
    model = Ride
    success_url = reverse_lazy('pages:home')
