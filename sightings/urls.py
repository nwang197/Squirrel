from django.urls import path

from . import views

urlpatterns = [
    path('',views.all_Ss),
    path('add', views.addsquirrel),
    path('<str:Unique_Squirrel_ID>', views.edit_squirrel),
    path("stats/",views.stats),
    ]
