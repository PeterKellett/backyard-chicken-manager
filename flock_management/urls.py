from django.urls import path
from . import views


urlpatterns = [
    path('', views.flocks, name='flocks'),
    path('add_flock/', views.add_flock, name='add_flock'),
    path('bird_removal/', views.bird_removal, name='bird_removal'),
    path('hens_quantity/', views.get_hens_quantity, name='hens_quantity')
]
