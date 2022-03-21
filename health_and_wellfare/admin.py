from django.contrib import admin
from .models import Supplements


# Register your models here.
class SupplementsAdmin(admin.ModelAdmin):
    """Admin layout for EggCollection Admin table"""
    list_display = (
        'id',
        'farm_profile_id',
        'supplement_name',
        'qty_supplements'
    )


admin.site.register(Supplements, SupplementsAdmin)
