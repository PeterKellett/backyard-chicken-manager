from django.urls import path
from . import views


urlpatterns = [
    path('', views.sales_and_income, name='sales_and_income'),
    path('egg_delivery_sales', views.egg_delivery_sales, name='egg_delivery_sales'),
    path('egg_delivery_sales_dashboard', views.egg_delivery_sales_dashboard, name='egg_delivery_sales_dashboard'),
    path('egg_collection_sales', views.egg_collection_sales, name='egg_collection_sales'),
    # path('egg_collection_sales_dashboard', views.egg_collection_sales_dashboard, name='egg_collection_sales_dashboard'),
    path('egg_roadside_sales', views.egg_roadside_sales, name='egg_roadside_sales'),
    path('egg_market_sales', views.egg_market_sales, name='egg_market_sales'),
    path('bird_sales', views.bird_sales, name='bird_sales'),
    path('customers', views.customers, name='customers')
]
