from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel

def plotmap(request):
    pinpoints = Squirrel.objects.all().order_by('?')[:100]
    context = {
        'pinpoints': pinpoints
        }
    return render(request, 'map/map.html', context)
