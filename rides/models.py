from django.db import models

# Create your models here.


class Ride(models.Model):
    ride_name = models.CharField(
        max_length=100, blank=False, null=False, unique=True)

    class Meta:
        ordering = ('ride_name',)

    def __str__(self):
        return self.ride_name.title()
