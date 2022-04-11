from django.urls import path
from . import views


urlpatterns = [
    path('', views.supplements, name='supplements'),
    path('medicines/', views.medicines, name='medicines'),
    path('get_medicines/', views.get_medicines, name='get_medicines'),
    path('get_diseases/', views.get_diseases, name='get_diseases'),
    path('vaccines/', views.vaccines, name='vaccines'),
    path('get_vaccines/', views.get_vaccines, name='get_vaccines'),
    path('get_viruses/', views.get_viruses, name='get_viruses')
    # path('vaccines', views.vaccines, name='vaccines')
]
