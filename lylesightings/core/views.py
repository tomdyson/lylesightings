from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Sighting


def index(request):
    sightings = Sighting.objects.order_by('-datetime')
    paginator = Paginator(sightings, 10) # Show 10 sightings per page
    page = request.GET.get('page')
    paged_sightings = paginator.get_page(page)
    context = {
        'sightings': paged_sightings,
        'google_maps_key': settings.GOOGLE_MAPS_KEY
    }
    return render(request, 'index.html', context)

def detail(request, sighting):
    sighting = Sighting.objects.get(id=sighting)
    context = {
        'sighting': sighting,
        'google_maps_key': settings.GOOGLE_MAPS_KEY
    }
    return render(request, 'detail.html', context)

def map(request):
    sightings = Sighting.objects.exclude(location__isnull=True).order_by('-datetime')
    latest_sighting = sightings[0]
    context = {
        'sightings': sightings,
        'latest_sighting': latest_sighting,
        'google_maps_key': settings.GOOGLE_MAPS_KEY
    }
    return render(request, 'map.html', context)

def about(request):
    return render(request, 'about.html')