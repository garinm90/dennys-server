from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from rides.models import Ride
from .models import Customer
from .serializers import CustomerSerializer
from .forms import RideForm
from rest_framework import viewsets, generics


# Create your views here.


# class CustomerViewSet(generics.ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer


# class RideViewSet(generics.ListCreateAPIView):
#     queryset = Ride.objects.all()
#     serializer_class = RideSerializer
class CustomerList(ListView):
    model = Customer
    context_object_name = 'customers'


class CustomerDetail(DetailView):
    model = Customer
    context_object_name = 'customer'


class CustomerCreate(CreateView):
    model = Customer
    fields = ('customer_name', 'customer_email',
              'customer_company', 'customer_phonenumber')


class CustomerUpdate(UpdateView):
    model = Customer
    fields = ('customer_name', 'customer_email',
              'customer_company', 'customer_phonenumber', 'customer_rides')


class CustomerUpdateRide(UpdateView):
    model = Customer
    form_class = RideForm


class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('pages:home')


class CustomerRideList(ListView):
    context_object_name = 'ride_list'
    template_name = 'customers/customer_rides.html'

    def get_queryset(self):
        self.customer = get_object_or_404(
            Customer, pk=self.kwargs['pk'])
        return Ride.objects.filter(customers=self.customer)
