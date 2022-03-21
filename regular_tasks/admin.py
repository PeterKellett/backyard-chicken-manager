from django.contrib import admin
from .models import EggCollection, FeedingTime, CoopCleaning, Feeds, Disinfectants


class DisinfectantsAdmin(admin.ModelAdmin):
    """Admin layout for Disinfectants Admin table"""
    list_display = (
        'id',
        'disinfectant_name',
    )


class FeedsAdmin(admin.ModelAdmin):
    """Admin layout for EggCollection Admin table"""
    list_display = (
        'id',
        'farm_profile_id',
        'feed_name',
        'qty_food'
    )


# Register your models here.
class EggCollectionAdmin(admin.ModelAdmin):
    """Admin layout for EggCollection Admin table"""
    list_display = (
        'id',
        'date',
        # 'farm_profile_id',
        'flock_id',
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
        'notes'
    )


class FeedingTimeAdmin(admin.ModelAdmin):
    """Admin layout for EggCollection Admin table"""
    list_display = (
        'id',
        'date',
        # 'farm_profile_id',
        'flock_id',
        'feed_type_id',
        'amount_food_rem',
        'amount_food_added',
        'amount_water_rem',
        'amount_water_added',
        'notes'
    )


class CoopCleaningAdmin(admin.ModelAdmin):
    """Admin layout for EggCollection Admin table"""
    list_display = (
        'id',
        'date',
        # 'coop_id',
        'disinfected',
        'disinfectant',
        'notes'
    )


admin.site.register(EggCollection, EggCollectionAdmin)
admin.site.register(FeedingTime, FeedingTimeAdmin)
admin.site.register(CoopCleaning, CoopCleaningAdmin)
admin.site.register(Feeds, FeedsAdmin)
admin.site.register(Disinfectants, DisinfectantsAdmin)
