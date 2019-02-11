from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Ride
from customers.models import Customer


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


class RidesCustomer(ListView):
    model = Customer
    template_name = 'rides/customer_rides.html'
    context_object_name = 'rides'

    def get_context_data(self, **kwargs):
        context = super(RidesCustomer, self).get_context_data(**kwargs)
        self.customer = get_object_or_404(
            Customer, pk=self.kwargs['pk'])
        context['rides'] = Ride.objects.filter(customers=self.customer)
        context['customer'] = self.customer
        print(context)
        return context
