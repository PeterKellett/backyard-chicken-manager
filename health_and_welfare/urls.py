from django.urls import path
from . import views


urlpatterns = [
    path('', views.supplements, name='supplements'),
    path('medicines/', views.medicines, name='medicines'),
    path('get_medicines/', views.get_medicines, name='get_medicines')
    # path('vaccines', views.vaccines, name='vaccines')
]
