from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('onboard_personal', views.onboard_personal, name='onboard_personal'),
    path('onboard_flock', views.onboard_flock, name='onboard_flock'),
    path('onboard_produce', views.onboard_produce, name='onboard_produce'),
    path('onboard_stock', views.onboard_stock, name='onboard_stock'),
    path('get_onboarding_data', views.get_onboarding_data, name='get_onboarding_data'),
]
