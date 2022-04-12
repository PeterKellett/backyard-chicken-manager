from django.contrib import admin
from .models import PurchasesCategory, Purchases


class PurchasesCategoryAdmin(admin.ModelAdmin):
    """Admin layout for Purchases Categories Admin table"""
    list_display = (
        'id',
        'category'
    )


class PurchasesAdmin(admin.ModelAdmin):
    """Admin layout for Medicines Admin table"""
    list_display = (
        'id',
        'farm_profile_id',
        'product'
    )


admin.site.register(PurchasesCategory, PurchasesCategoryAdmin)
admin.site.register(Purchases, PurchasesAdmin)
