from django import forms
from dal import autocomplete
from .models import Job


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('job_number', 'customer', 'ride', 'job_image')
        widgets = {
            'customer': autocomplete.ModelSelect2(url='pages:customer-autocomplete'),
            'ride': autocomplete.ModelSelect2(url='pages:ride-autocomplete')

        }
