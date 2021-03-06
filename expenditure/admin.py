from django.contrib import admin
from .models import PaymentMethods, PurchasesCategory, Purchases, Withdrawals


class PaymentMethodsAdmin(admin.ModelAdmin):
    """Admin layout for Payment Methods Admin table"""
    list_display = (
        'id',
        'payment_method'
    )


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


class WithdrawalsAdmin(admin.ModelAdmin):
    """Admin layout for Medicines Admin table"""
    list_display = (
        'id',
        'farm_profile_id',
        'amount_withdrawn'
    )


admin.site.register(PaymentMethods, PaymentMethodsAdmin)
admin.site.register(PurchasesCategory, PurchasesCategoryAdmin)
admin.site.register(Purchases, PurchasesAdmin)
admin.site.register(Withdrawals, WithdrawalsAdmin)
