from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Squirrel
from .forms import SForm
from django.db.models import Count

def all_Ss(request):
    Squirrels = Squirrel.objects.all()
    context = {
                'Squirrels': Squirrels,
            }
    return render(request, '/sightings/all.html', context)

def addsquirrel(request):
    if request.method == 'POST':
        form = SForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/add')
    else:
        form = SForm
    context = {
            'form':form,
            }
    return render(request,'sightings/edit.html',context)
def squirrel_details(request, Unique_Squirrel_ID ):
    squirrel  = Squirrel.objects.get(id= Unique_Squirrel_ID)
    return HttpResponse(squirrel.Unique_Squirrel_ID)


def edit_squirrel(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(id=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SForm(request.POST, instance= squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{Unique_Squirrel_ID}')
    else:
        form = SForm(instance = squirel)

    context = {
            'form'：form,
            }

    return render(request,'/sightings/edit.html',context)

def stats(request):
    agelist = Squirrel.objects.values('age').annotate(count=Count('age'))
    colorlist = Squirrel.objects.values('color').annotate(count=Count('color'))
    climbinglist = Squirrel.objects.values('climbing').annotate(count=Count('climbing'))
    runninglist = Squirrel.objects.values('running').annotate(count=Count('running'))
    chasinglist = Squirrel.objects.values('chasing').annotate(count=Count('chasing'))
    context={
                'agelist':agelist,
                'furcolorlist':colorlist,
                'climbinglist':climbinglist,
                'runninglist':runninglist,
                'chasinglist':chasinglist,
            }
    return render(request, 'sightings/stats.html',context)




# Create your views here.
