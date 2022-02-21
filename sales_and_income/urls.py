from django.urls import path
from . import views


urlpatterns = [
    path('', views.sales_and_income, name='sales_and_income'),
    path('delivery_sales', views.delivery_sales, name='delivery_sales'),
    path('collection_sales', views.collection_sales, name='collection_sales'),
    path('roadside_sales', views.roadside_sales, name='roadside_sales'),
    path('market_sales', views.market_sales, name='market_sales'),
    path('bird_sales', views.bird_sales, name='bird_sales'),
    path('customers', views.customers, name='customers')
]
