from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from customers.models import Customer, Ride
from customers.serializers import CustomerSerializer, RideSerializer
from rest_framework import viewsets, generics

# Create your views here.


# class CustomerViewSet(generics.ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer


# class RideViewSet(generics.ListCreateAPIView):
#     queryset = Ride.objects.all()
#     serializer_class = RideSerializer


class RideCreate(CreateView):
    model = Ride
    fields = ('ride_name',)
    success_url = reverse_lazy('pages:home')


class CustomerCreate(CreateView):
    model = Customer
    fields = ('customer_name', 'customer_email',
              'customer_company', 'customer_phonenumber')
