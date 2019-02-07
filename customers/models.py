from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(blank=True)
    customer_company = models.CharField(
        max_length=254, unique=True, blank=True)
    customer_phonenumber = PhoneNumberField(
        blank=True, verbose_name='Phone Number')
    customer_rides = models.ManyToManyField(
        'rides.Ride', related_name='customers', blank=True)

    class Meta:
        ordering = ('customer_name', )

    def __str__(self):
        return self.customer_name.title()

    def get_absolute_url(self):
        return reverse('customers:detail_customer', args=[str(self.id)])
