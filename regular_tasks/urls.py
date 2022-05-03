from django.urls import path
from . import views


urlpatterns = [
    path('', views.egg_collection, name='egg_collection'),
    path('get_feeds/', views.get_feeds, name='get_feeds'),
    path('feeding_time/', views.feeding_time, name='feeding_time'),
    path('get_disinfectants/', views.get_disinfectants, name='get_disinfectants'),
    path('coop_cleaning/', views.coop_cleaning, name='coop_cleaning'),
    path('trays_quantity/', views.get_trays_quantity, name='trays_quantity'),
    path('hens_quantity/', views.get_hens_quantity, name='hens_quantity')
]
