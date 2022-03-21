from django.contrib import admin
from .models import Flocks, Coops


# Register your models here.
class FlocksAdmin(admin.ModelAdmin):
    """Admin model"""
    list_display = (
        'id',
        'farm_profile_id',
        'flock_name',
        'identifier',
        'breed',
        'hens_qty',
        'chicks_qty',
        'cocks_qty'
        )


class CoopsAdmin(admin.ModelAdmin):
    """Admin model"""
    list_display = (
        'id',
        'farm_profile_id',
        'coop_name'
        )


admin.site.register(Flocks, FlocksAdmin)
admin.site.register(Coops, CoopsAdmin)
