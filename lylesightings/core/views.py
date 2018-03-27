from django.shortcuts import render
from django.conf import settings

from .models import Sighting


def index(request):
    latest_sightings = Sighting.objects.order_by('-datetime')[:10]
    context = {
        'latest_sightings': latest_sightings,
        'google_maps_key': settings.GOOGLE_MAPS_KEY
    }
    return render(request, 'index.html', context)
