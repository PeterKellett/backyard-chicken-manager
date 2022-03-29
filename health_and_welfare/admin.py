from django.contrib import admin
from .models import Supplements, SupplementsName, Medicines, MedicinesName, Vaccines, VaccinesName, DiseasesName


class SupplementsAdmin(admin.ModelAdmin):
    """Admin layout for Supplements Admin table"""
    list_display = (
        'id',
        'farm_profile_id',
        'supplement_name'
    )


class SupplementsNameAdmin(admin.ModelAdmin):
    """Admin layout for Supplement Names Admin table"""
    list_display = (
        'id',
        'supplement_name'
    )


class MedicinesAdmin(admin.ModelAdmin):
    """Admin layout for Medicines Admin table"""
    list_display = (
        'id',
        'farm_profile_id',
        'medicine_name'
    )


class MedicinesNameAdmin(admin.ModelAdmin):
    """Admin layout for Medicine Names Admin table"""
    list_display = (
        'id',
        'medicine_name'
    )


class VaccinesAdmin(admin.ModelAdmin):
    """Admin layout for Vaccines Admin table"""
    list_display = (
        'id',
        'farm_profile_id',
        'vaccine_name'
    )


class VaccinesNameAdmin(admin.ModelAdmin):
    """Admin layout for Vaccine Names Admin table"""
    list_display = (
        'id',
        'vaccine_name'
    )


class DiseasesNameAdmin(admin.ModelAdmin):
    """Admin layout for Disease Names Admin table"""
    list_display = (
        'id',
        'disease_name'
    )


admin.site.register(Supplements, SupplementsAdmin)
admin.site.register(SupplementsName, SupplementsNameAdmin)
admin.site.register(Medicines, MedicinesAdmin)
admin.site.register(MedicinesName, MedicinesNameAdmin)
admin.site.register(Vaccines, VaccinesAdmin)
admin.site.register(VaccinesName, VaccinesNameAdmin)
admin.site.register(DiseasesName, DiseasesNameAdmin)
