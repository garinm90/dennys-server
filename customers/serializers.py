from rest_framework import serializers
from customers.models import Customer, Ride


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('ride_name', )
