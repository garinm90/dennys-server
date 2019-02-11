from django import forms
from dal import autocomplete
from .models import Customer
from rides.models import Ride


class RideForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_name', 'customer_rides')
        customer_name = forms.CharField(label='Customer name', max_length=100)
        widgets = {
            'customer_rides': autocomplete.ModelSelect2Multiple(url='customers:add_rides')
        }
