from django.urls import path

from . import views


urlpatterns = [
    path('',views.all_Ss),
    path('add', views.addsquirrel),
    path('<Unique_Squirrel_ID>', views.squirrel_details),
    path('edit', views.edit_squirrel),
    path('stats',views.stats),
            ]