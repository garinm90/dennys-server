from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Ride(models.Model):
    ride_name = models.CharField(
        max_length=100, blank=False, null=False, unique=True)

    class Meta:
        ordering = ('ride_name',)

    def __str__(self):
        return self.ride_name.title()


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(blank=True)
    customer_company = models.CharField(
        max_length=254, unique=True, blank=True)
    customer_phonenumber = PhoneNumberField(blank=True)
    customer_rides = models.ManyToManyField(
        Ride, related_name='customers', blank=True)

    class Meta:
        ordering = ('customer_name', )

    def __str__(self):
        return self.customer_name.title()
