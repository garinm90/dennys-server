from django.views.generic import TemplateView
from dal import autocomplete
from rides.models import Ride


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class RideAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Ride.objects.all()
        if self.q:
            qs = qs.filter(ride_name__icontains=self.q)
        return qs
