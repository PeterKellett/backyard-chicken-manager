from django.contrib import admin
from .models import FarmType, UserProfile, FarmProfile, Breed, FarmPurpose


# Register your models here.
class FarmTypeAdmin(admin.ModelAdmin):
    """Admin model"""
    list_display = (
        'id',
        'type',
    )


class BreedsAdmin(admin.ModelAdmin):
    """Admin model"""
    list_display = (
        'id',
        'type',
    )


class FarmPurposeAdmin(admin.ModelAdmin):
    """Admin model"""
    list_display = (
        'id',
        'type',
    )


class UserProfileAdmin(admin.ModelAdmin):
    """Admin layout for UserProfile table"""
    list_display = (
        'id',
        'user',
        'first_name',
        'last_name',
        'city_country',
    )


class FarmProfileAdmin(admin.ModelAdmin):
    """Admin layout for FarmProfile table"""
    list_display = (
        'id',
        'user_profile_id',
        'farm_business_name',
        'farm_type_id',
        'farm_sales_roadside',
        'farm_sales_markets',
        'farm_sales_deliveries',
        'farm_sales_collections',
        'sales_units_single_eggs',
        'sales_units_half_dozen_carton',
        'sales_units_dozen_carton',
        'sales_units_trays',
        'trays_quantity',
        'eggs_in_stock',
        'current_balance',
        'onboard_complete'
    )


admin.site.register(FarmType, FarmTypeAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(FarmProfile, FarmProfileAdmin)
admin.site.register(Breed, BreedsAdmin)
admin.site.register(FarmPurpose, FarmPurposeAdmin)
