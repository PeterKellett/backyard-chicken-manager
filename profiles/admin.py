from django.contrib import admin
from .models import FarmType, UserProfile, FarmProfile


# Register your models here.
class FarmTypeAdmin(admin.ModelAdmin):
    list_display = (
        'type',
    )


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
    )


class FarmProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'farm_name',
        'farm_type',
        'farm_sales_roadside',
        'farm_sales_markets',
        'farm_sales_deliveries',
        'farm_sales_collections',
        'eggs_in_stock',
        'current_balance',
    )


admin.site.register(FarmType, FarmTypeAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(FarmProfile, FarmProfileAdmin)
