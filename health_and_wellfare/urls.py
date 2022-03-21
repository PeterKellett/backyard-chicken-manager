from django.urls import path
from . import views


urlpatterns = [
    path('', views.health_and_wellfare, name='health_and_wellfare')
]
