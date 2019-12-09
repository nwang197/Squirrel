from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Squirrel
from .forms import SForm
from django.db.models import Count

def all_Ss(request):
    if request.method == "GET":
         Squirrels = Squirrel.objects.all()
         context = {
                'Squirrels': Squirrels,
                     }
    return render(request, 'sightings/all.html', context)

def addsquirrel(request):
    if request.method == 'POST':
        form = SForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = SForm
    context = {
            'form':form,
            }
    return render(request,'sightings/edit.html',context)
#def squirrel_details(request, Unique_Squirrel_ID ):
#    squirrel  = Squirrel.objects.get(id= Unique_Squirrel_ID)
#    return HttpResponse(squirrel.Unique_Squirrel_ID)


def edit_squirrel(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SForm(request.POST, instance= squirrel)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = SForm(instance = squirrel)

    context = {
            'form':form,
            }

    return render(request,'sightings/edit.html',context)

def stats(request):
    agelist = Squirrel.objects.values('Age').annotate(count=Count('Age'))
    colorlist = Squirrel.objects.values('Primary_Fur_Color').annotate(count=Count('Primary_Fur_Color'))
    climbinglist = Squirrel.objects.values('Climbing').annotate(count=Count('Climbing'))
    runninglist = Squirrel.objects.values('Running').annotate(count=Count('Running'))
    chasinglist = Squirrel.objects.values('Chasing').annotate(count=Count('Chasing'))
    context={
                'agelist':agelist,
                'furcolorlist':colorlist,
                'climbinglist':climbinglist,
                'runninglist':runninglist,
                'chasinglist':chasinglist,
            }
    return render(request, 'sightings/stats.html',context)


