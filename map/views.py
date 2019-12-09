from django.shortcuts import render
from sightings.models import Squirrel


def map(request):
    pinpoints = Squirrel.objects.all()[:100]
    context = {
        'pinpoints': pinpoints,
        }
    return render(request, 'map/map.html', context)

