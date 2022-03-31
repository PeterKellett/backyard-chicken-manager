from django.urls import path
from . import views


urlpatterns = [
    path('', views.supplements, name='supplements'),
    path('medicines/', views.medicines, name='medicines')
    # path('vaccines', views.vaccines, name='vaccines')
]
