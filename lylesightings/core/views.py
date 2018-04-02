from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Sighting


def index(request):
    latest_sightings = Sighting.objects.order_by('-datetime')
    paginator = Paginator(latest_sightings, 10) # Show 10 sightings per page
    page = request.GET.get('page')
    paged_sightings = paginator.get_page(page)
    context = {
        'latest_sightings': paged_sightings,
        'google_maps_key': settings.GOOGLE_MAPS_KEY
    }
    return render(request, 'index.html', context)
