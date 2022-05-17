from django.contrib import admin
from .models import DiseasesName, AdministrationMethod, SupplementsName, Supplements, MedicinesName, Medicines, VaccinesName, Vaccines, VirusesName


class DiseasesNameAdmin(admin.ModelAdmin):
    """Admin layout for Disease Names Admin table"""
    list_display = (
        'id',
        'disease_name'
    )


class AdministrationMethodAdmin(admin.ModelAdmin):
    """Admin layout for dose administration method Admin table"""
    list_display = (
        'id',
        'administration_method'
    )


class SupplementsNameAdmin(admin.ModelAdmin):
    """Admin layout for Supplement Names Admin table"""
    list_display = (
        'id',
        'supplement_name',
        'supplement_in_stock'
    )


class SupplementsAdmin(admin.ModelAdmin):
    """Admin layout for Supplements Admin table"""
    list_display = (
        'id',
        'farm_profile',
        'date',
        'flock',
        'supplement_name',
        'qty_hens',
        'qty_chicks',
        'qty_cocks',
        'dosage_amount',
        'dose_per_bird',
        'vet_administered',
        'vet_name',
        'notes',
        'images'
    )


class MedicinesNameAdmin(admin.ModelAdmin):
    """Admin layout for Medicine Names Admin table"""
    list_display = (
        'id',
        'farm_profile',
        'medicine_name'
    )


class MedicinesAdmin(admin.ModelAdmin):
    """Admin layout for Medicines Admin table"""
    list_display = (
        'id',
        'farm_profile',
        'date',
        'flock',
        'medicine_name',
        'disease_protected_against',
        'qty_hens',
        'qty_chicks',
        'qty_cocks',
        'dosage_amount',
        'dose_per_bird',
        'administration_method',
        'vet_administered',
        'vet_name',
        'notes',
        'images'
    )


class VirusesNameAdmin(admin.ModelAdmin):
    """Admin layout for Virus Names Admin table"""
    list_display = (
        'id',
        'virus_name'
    )


class VaccinesNameAdmin(admin.ModelAdmin):
    """Admin layout for Vaccine Names Admin table"""
    list_display = (
        'id',
        'vaccine_name'
    )


class VaccinesAdmin(admin.ModelAdmin):
    """Admin layout for Vaccines Admin table"""
    list_display = (
        'id',
        'farm_profile_id',
        'date',
        'flock',
        'vaccine_name',
        'virus_protected_against',
        'qty_hens',
        'qty_chicks',
        'qty_cocks',
        'dosage_amount',
        'dose_per_bird',
        'administration_method',
        'vet_administered',
        'vet_name',
        'notes',
        'images'

    )


admin.site.register(DiseasesName, DiseasesNameAdmin)
admin.site.register(AdministrationMethod, AdministrationMethodAdmin)
admin.site.register(SupplementsName, SupplementsNameAdmin)
admin.site.register(Supplements, SupplementsAdmin)
admin.site.register(MedicinesName, MedicinesNameAdmin)
admin.site.register(Medicines, MedicinesAdmin)
admin.site.register(VaccinesName, VaccinesNameAdmin)
admin.site.register(Vaccines, VaccinesAdmin)
admin.site.register(VirusesName, VirusesNameAdmin)
