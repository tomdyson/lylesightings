from django.shortcuts import render

from .models import Sighting


def index(request):
    latest_sightings = Sighting.objects.order_by('-datetime')[:10]
    context = {'latest_sightings': latest_sightings}
    return render(request, 'index.html', context)
