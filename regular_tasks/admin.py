from django.contrib import admin
from .models import EggCollection, FeedingTime, CoopCleaning, Foods, Disinfectants


class DisinfectantsAdmin(admin.ModelAdmin):
    """Admin layout for Disinfectants Admin table"""
    list_display = (
        'disinfectant_name',
    )


class FoodsAdmin(admin.ModelAdmin):
    """Admin layout for EggCollection Admin table"""
    list_display = (
        'farm_profile',
        'feed_name',
        'qty_food'
    )


# Register your models here.
class EggCollectionAdmin(admin.ModelAdmin):
    """Admin layout for EggCollection Admin table"""
    list_display = (
        # 'farm_profile',
        'date',
        # 'flock',
        'qty_egg_trays',
        'qty_egg_singles',
        'qty_total_eggs_laid',
        'qty_eggs_damaged',
        'qty_eggs_broken',
        'qty_eggs_personal_use',
        'qty_eggs_given_free',
        'weight_total_eggs_laid',
        'avg_egg_weight',
        'qty_saleable_eggs',
        'egg_collection_notes'
    )


class FeedingTimeAdmin(admin.ModelAdmin):
    """Admin layout for EggCollection Admin table"""
    list_display = (
        # 'farm_profile',
        'date',
        # 'flock',
        'feed_type',
        'amount_food_rem',
        'amount_food_added',
        'amount_water_rem',
        'amount_water_added',
        'feeding_notes'
    )


class CoopCleaningAdmin(admin.ModelAdmin):
    """Admin layout for EggCollection Admin table"""
    list_display = (
        # 'coop',
        'date',
        'disinfected',
        'disinfectant',
        'coop_cleaning_notes'
    )


admin.site.register(EggCollection, EggCollectionAdmin)
admin.site.register(FeedingTime, FeedingTimeAdmin)
admin.site.register(CoopCleaning, CoopCleaningAdmin)
admin.site.register(Foods, FoodsAdmin)
admin.site.register(Disinfectants, DisinfectantsAdmin)
