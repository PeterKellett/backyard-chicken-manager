from django.urls import path
from . import views


urlpatterns = [
    path('', views.egg_collection, name='regular_tasks'),
    path('feeding_time/', views.feeding_time, name='feeding_time'),
    path('coop_cleaning/', views.coop_cleaning, name='coop_cleaning')
]
