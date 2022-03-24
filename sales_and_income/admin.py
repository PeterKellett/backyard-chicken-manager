from django.contrib import admin
from .models import EggRoadsideSales, EggCollectionSales, EggDeliverySalesDashboard, EggDeliverySales, EggMarketSales

# Register your models here.
class EggRoadsideSalesAdmin(admin.ModelAdmin):
    """Admin layout for Egg Roadside Sales Admin table"""
    list_display = (
        'id',
        'date',
        # 'farm_profile_id',
        'single_egg_price',
        'half_dozen_eggs_price',
        'ten_eggs_price',
        'dozen_eggs_price',
        'trays_of_eggs_price',
        'qty_single_eggs_remaining',
        'qty_single_eggs_added',
        'qty_half_dozen_egg_boxes_remaining',
        'qty_half_dozen_egg_boxes_added',
        'qty_ten_egg_boxes_remaining',
        'qty_ten_egg_boxes_added',
        'qty_dozen_egg_boxes_remaining',
        'qty_dozen_egg_boxes_added',
        'qty_trays_of_eggs_remaining',
        'qty_trays_of_eggs_added',
        'amount_paid_eggs_roadside',
        'loses_eggs_roadside',
        'notes'
    )


class EggDeliverySalesDashboardAdmin(admin.ModelAdmin):
    """Admin layout for Egg Delivery Sales Dashboard Admin table"""
    list_display = (
        'id',
        'date',
        # 'farm_profile_id',
        'breakages_and_loses_eggs_delivery'
    )


class EggDeliverySalesAdmin(admin.ModelAdmin):
    """Admin layout for Egg Delivery Sales Admin table"""
    list_display = (
        'id',
        'date',
        # 'farm_profile_id',
        'qty_sold_eggs_delivery',
        'qty_given_free_eggs_delivery',
        'amount_paid_eggs_delivery'
    )


admin.site.register(EggRoadsideSales, EggRoadsideSalesAdmin)
admin.site.register(EggDeliverySalesDashboard, EggDeliverySalesDashboardAdmin)
admin.site.register(EggDeliverySales, EggDeliverySalesAdmin)
