from django import forms
from dal import autocomplete
from .models import Customer
from rides.models import Ride


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('__all__')
        widgets = {
            'customer_rides': autocomplete.ModelSelect2Multiple(url='pages:ride-autocomplete')
        }
