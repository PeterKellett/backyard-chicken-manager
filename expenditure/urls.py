from django.urls import path
from . import views


urlpatterns = [
    path('', views.purchases, name='purchases'),
    path('get_purchase_categories/', views.get_purchase_categories, name='get_purchase_categories')
]
