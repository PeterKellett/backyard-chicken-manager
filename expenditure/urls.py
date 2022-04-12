from django.urls import path
from . import views


urlpatterns = [
    path('', views.purchases, name='purchases'),
    path('get_purchase_categories/', views.get_purchase_categories, name='get_purchase_categories'),
    path('withdrawals', views.withdrawals, name='withdrawals'),
    path('get_payment_methods', views.get_payment_methods, name='get_payment_methods')
]
