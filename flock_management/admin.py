from django.contrib import admin
from .models import Flocks


# Register your models here.
class FlocksAdmin(admin.ModelAdmin):
    """Admin model"""
    list_display = (
        'farm_id',
        'flock_name',
        'identifier',
        'breed',
        'coop_name',
        'hens_qty',
        'chicks_qty',
        'cocks_qty'
        )


admin.site.register(Flocks, FlocksAdmin)
