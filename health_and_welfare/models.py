from django.db import models
from profiles.models import FarmProfile
from flock_management.models import Flocks
from django.utils import timezone


class AdministrationMethod(models.Model):
    """Model used for identifying methods of administering doses"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Administration Methods'
    administration_method = models.CharField(max_length=50,
                                             null=True,
                                             blank=True)

    def __str__(self):
        return self.administration_method


class SupplementsName(models.Model):
    """Model used for Supplement names"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Supplement Names'
    farm_profile = models.ForeignKey(FarmProfile,
                                     null=True,
                                     blank=True,
                                     default=None,
                                     on_delete=models.CASCADE)
    supplement_name = models.CharField(max_length=50,
                                       null=False,
                                       blank=False)
    supplement_in_stock = models.DecimalField(max_digits=6,
                                              decimal_places=2,
                                              null=True,
                                              blank=True)

    def __str__(self):
        return self.supplement_name


class Supplements(models.Model):
    """Model used for storing Supplements data"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Supplements'
    farm_profile = models.ForeignKey(FarmProfile,
                                     null=False,
                                     blank=False,
                                     on_delete=models.CASCADE)
    date = models.DateTimeField(null=False,
                                blank=False)
    flock = models.ForeignKey(Flocks,
                              null=False,
                              blank=False,
                              on_delete=models.CASCADE)
    supplement_name = models.CharField(max_length=50,
                                       null=False,
                                       blank=False)
    qty_hens = models.IntegerField(null=True,
                                   blank=True)
    qty_chicks = models.IntegerField(null=True,
                                     blank=True)
    qty_cocks = models.IntegerField(null=True,
                                    blank=True)
    dosage_amount = models.DecimalField(max_digits=5,
                                        decimal_places=2,
                                        null=False,
                                        blank=False)
    dose_per_bird = models.DecimalField(max_digits=5,
                                        decimal_places=2,
                                        null=False,
                                        blank=False)
    vet_administered = models.BooleanField(default=False)
    vet_name = models.CharField(max_length=50,
                                null=True,
                                blank=True)

    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")


class DiseasesName(models.Model):
    """Model used for Disease names"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Disease Names'
    farm_profile = models.ForeignKey(FarmProfile,
                                     null=True,
                                     blank=True,
                                     on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=50,
                                    null=True,
                                    blank=True)

    def __str__(self):
        return self.disease_name


class MedicinesName(models.Model):
    """Model used for Medicine names"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Medicine Names'
    farm_profile = models.ForeignKey(FarmProfile,
                                     null=True,
                                     blank=True,
                                     on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=50,
                                     null=True,
                                     blank=True)

    def __str__(self):
        return self.medicine_name


class Medicines(models.Model):
    """Model used for storing Medicines data"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Medicines'
    farm_profile = models.ForeignKey(FarmProfile,
                                     null=False,
                                     blank=False,
                                     on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now,
                                null=False,
                                blank=False)
    flock = models.ForeignKey(Flocks,
                              null=False,
                              blank=False,
                              on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=50,
                                     null=False,
                                     blank=False)
    disease_protected_against = models.CharField(max_length=50,
                                                 null=False,
                                                 blank=False)
    qty_hens = models.IntegerField(null=True,
                                   blank=True)
    qty_chicks = models.IntegerField(null=True,
                                     blank=True)
    qty_cocks = models.IntegerField(null=True,
                                    blank=True)
    qty_total = models.IntegerField(null=True,
                                    blank=True)
    dosage_amount = models.DecimalField(max_digits=6,
                                        decimal_places=2,
                                        null=False,
                                        blank=False)
    dose_per_bird = models.DecimalField(max_digits=5,
                                        decimal_places=2,
                                        null=False,
                                        blank=False)
    administration_method = models.ForeignKey(AdministrationMethod,
                                              null=True,
                                              blank=True,
                                              on_delete=models.SET_NULL)
    vet_administered = models.BooleanField(default=False)
    vet_name = models.CharField(max_length=50,
                                null=True,
                                blank=True)

    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")


class VirusesName(models.Model):
    """Model used for Virus names"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Virus Names'
    farm_profile = models.ForeignKey(FarmProfile,
                                     null=True,
                                     blank=True,
                                     on_delete=models.CASCADE)
    virus_name = models.CharField(max_length=50,
                                  null=True,
                                  blank=True)

    def __str__(self):
        return self.virus_name


class VaccinesName(models.Model):
    """Model used for Vaccine names"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Vaccine Names'
    farm_profile = models.ForeignKey(FarmProfile,
                                     null=True,
                                     blank=True,
                                     on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=50,
                                    null=True,
                                    blank=True)

    def __str__(self):
        return self.vaccine_name


class Vaccines(models.Model):
    """Model used for storing Vaccines data"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Vaccines'
    farm_profile = models.ForeignKey(FarmProfile,
                                     null=False,
                                     blank=False,
                                     on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now,
                                null=False,
                                blank=False)
    flock = models.ForeignKey(Flocks,
                              null=False,
                              blank=False,
                              on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=50,
                                    null=False,
                                    blank=False)
    virus_protected_against = models.CharField(max_length=50,
                                               null=True,
                                               blank=True)
    qty_hens = models.IntegerField(null=True,
                                   blank=True)
    qty_chicks = models.IntegerField(null=True,
                                     blank=True)
    qty_cocks = models.IntegerField(null=True,
                                    blank=True)
    qty_total = models.IntegerField(null=True,
                                    blank=True)
    dosage_amount = models.DecimalField(max_digits=6,
                                        decimal_places=2,
                                        null=True,
                                        blank=True)
    dose_per_bird = models.DecimalField(max_digits=5,
                                        decimal_places=2,
                                        null=False,
                                        blank=False)
    administration_method = models.ForeignKey(AdministrationMethod,
                                              null=True,
                                              blank=True,
                                              on_delete=models.SET_NULL)
    vet_administered = models.BooleanField(default=False)
    vet_name = models.CharField(max_length=50,
                                null=True,
                                blank=True)

    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")
