from django.urls import path

from . import views


urlpatterns = [
    path('',views.all_Ss),
    path('/sightings/add', views.addsquirrel),
    path('/sightings/<Unique_Squirrel_ID>', views.squirrel_details),
    path('/sightings/edit', views.edit_squirrel),
    path('/sightings/stats',views.stats),
            ]
