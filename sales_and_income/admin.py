from django.contrib import admin
from .models import EggRoadsideSales, EggCollectionSales, EggDeliverySalesDashboard, EggDeliverySales, EggMarketSales, Pricing, SalesType


class SalesTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type'
    )


class PricingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'farm_profile',
        'sales_type',
        'single_egg_price',
        'half_dozen_eggs_price',
        'ten_eggs_price',
        'dozen_eggs_price',
        'trays_of_eggs_price'
    )


# Register your models here.
class EggRoadsideSalesAdmin(admin.ModelAdmin):
    """Admin layout for Egg Roadside Sales Admin table"""
    list_display = (
        'id',
        'date',
        'farm_profile_id',
        'qty_single_eggs_in_stock',
        'qty_single_eggs_remaining',
        'qty_single_eggs_sold',
        'qty_single_eggs_added',
        'qty_half_dozen_egg_boxes_remaining',
        'qty_half_dozen_egg_boxes_added',
        'qty_half_dozen_egg_boxes_in_stock',
        'qty_half_dozen_egg_boxes_sold',
        'qty_ten_egg_boxes_remaining',
        'qty_ten_egg_boxes_added',
        'qty_ten_egg_boxes_in_stock',
        'qty_ten_egg_boxes_sold',
        'qty_dozen_egg_boxes_remaining',
        'qty_dozen_egg_boxes_added',
        'qty_dozen_egg_boxes_in_stock',
        'qty_dozen_egg_boxes_sold',
        'qty_trays_eggs_remaining',
        'qty_trays_eggs_added',
        'qty_trays_eggs_in_stock',
        'qty_trays_eggs_sold',
        'income',
        'income_deficit',
        'pricing',
        'losses_eggs_roadside',
        'notes',
        'images'
    )


class EggDeliverySalesDashboardAdmin(admin.ModelAdmin):
    """Admin layout for Egg Delivery Sales Dashboard Admin table"""
    list_display = (
        'id',
        'date',
        # 'farm_profile_id',
        'breakages_and_loses_eggs_delivery',
        'notes',
        'images'
    )


class EggDeliverySalesAdmin(admin.ModelAdmin):
    """Admin layout for Egg Delivery Sales Admin table"""
    list_display = (
        'id',
        'date',
        # 'farm_profile_id',
        'customer_name_eggs_delivery',
        'normal_order_qty_eggs_delivery',
        'delivery_due_date',
        'delivery_not_made',
        'delivery_not_made_reason',
        'qty_sold_eggs_delivery',
        'qty_given_free_eggs_delivery',
        'amount_paid_eggs_delivery',
        'balance_owed_eggs_delivery',
        'notes',
        'images'
    )


class EggCollectionSalesAdmin(admin.ModelAdmin):
    """Admin layout for Egg Collection Sales Admin table"""
    list_display = (
        'id',
        'date',
        # 'farm_profile_id',
        # 'customer_name_eggs_collection',
        'normal_order_qty_eggs_collection',
        'qty_sold_eggs_collection',
        'qty_given_free_eggs_collection',
        'amount_paid_eggs_collection',
        'balance_owed_eggs_collection',
        'breakages_and_loses_eggs_collection',
        'notes',
        'images'
    )


class EggMarketSalesAdmin(admin.ModelAdmin):
    """Admin layout for Egg Market Sales Admin table"""
    list_display = (
        'id',
        'date',
        # 'farm_profile_id',
        'venue_location_eggs_market',
        'single_egg_price',
        'half_dozen_eggs_price',
        'ten_eggs_price',
        'dozen_eggs_price',
        'trays_of_eggs_price',
        'qty_single_eggs_sold',
        'qty_half_dozen_egg_boxes_sold',
        'qty_ten_egg_boxes_sold',
        'qty_dozen_egg_boxes_sold',
        'qty_trays_of_eggs_sold',
        'amount_paid_eggs_market',
        'sales_amount_eggs_market',
        'sales_paid_difference_eggs_market',
        'loses_eggs_market',
        'notes',
        'images'
    )


admin.site.register(SalesType, SalesTypeAdmin)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(EggRoadsideSales, EggRoadsideSalesAdmin)
admin.site.register(EggDeliverySalesDashboard, EggDeliverySalesDashboardAdmin)
admin.site.register(EggDeliverySales, EggDeliverySalesAdmin)
admin.site.register(EggCollectionSales, EggCollectionSalesAdmin)
admin.site.register(EggMarketSales, EggMarketSalesAdmin)
