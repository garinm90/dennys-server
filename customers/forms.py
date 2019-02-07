from django import forms
from .models import Customer
from rides.models import Ride


class RideForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['customer_name', 'customer_email',
                   'customer_company', 'customer_phonenumber', 'customer_rides']
    rides = forms.ModelMultipleChoiceField(
        queryset=Ride.objects.all(),
        widget=forms.CheckboxSelectMultiple,

    )
