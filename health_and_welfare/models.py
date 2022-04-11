from django.db import models
from profiles.models import FarmProfile
from flock_management.models import Flocks


class Recipients(models.Model):
    """Model used for identifying recipients"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Recipients'
    recipients = models.CharField(max_length=50,
                                  null=True,
                                  blank=True)
    
    def __str__(self):
        return self.recipients


class DiseasesName(models.Model):
    """Model used for Disease names"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Disease Names'
    disease_name = models.CharField(max_length=50,
                                    null=True,
                                    blank=True)

    def __str__(self):
        return self.disease_name


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
                                     null=False,
                                     blank=False,
                                     on_delete=models.CASCADE)
    supplement_name = models.CharField(max_length=50,
                                       null=True,
                                       blank=True)
    supplement_in_stock = models.DecimalField(max_digits=6,
                                              decimal_places=2,
                                              null=True,
                                              blank=True)

class Supplements(models.Model):
    """Model used for storing Supplements data"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Supplements'
    farm_profile = models.ForeignKey(FarmProfile,
                                     null=False,
                                     blank=False,
                                     on_delete=models.CASCADE)
    supplement_name = models.CharField(max_length=50,
                                       null=True,
                                       blank=True)
    qty_supplements = models.DecimalField(max_digits=6,
                                          decimal_places=2,
                                          null=True,
                                          blank=True)


class MedicinesName(models.Model):
    """Model used for Medicine names"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Medicine Names'
    medicine_name = models.CharField(max_length=50,
                                     null=True,
                                     blank=True)

    def __str__(self):
        return self.medicine_name


class Medicines(models.Model):
    """Model used for storing Medicines data"""
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
    medicine_name = models.CharField(max_length=50,
                                     null=True,
                                     blank=True)
    disease_protected_against = models.CharField(max_length=50,
                                     null=True,
                                     blank=True)
    # disease_protected_against = models.ForeignKey(DiseasesName,
    #                                               null=True,
    #                                               blank=True,
    #                                               on_delete=models.CASCADE)
    qty_hens = models.IntegerField(null=True,
                                   blank=True)
    qty_chicks = models.IntegerField(null=True,
                                     blank=True)
    qty_cocks = models.IntegerField(null=True,
                                    blank=True)
    qty_total = models.IntegerField(null=True,
                                    blank=True)
    doseage_amount = models.DecimalField(max_digits=6,
                                         decimal_places=2,
                                         null=True,
                                         blank=True)
    administration_method = models.ForeignKey(AdministrationMethod,
                                              null=True,
                                              blank=True,
                                              on_delete=models.CASCADE)
    vet_administered = models.BooleanField(default=False)
    vet_name = models.CharField(max_length=50,
                                null=True,
                                blank=True)

    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")


class VaccinesName(models.Model):
    """Model used for Vaccine names"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Vaccine Names'
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
    vaccine_name = models.CharField(max_length=50,
                                    null=True,
                                    blank=True)
    qty_vaccines = models.DecimalField(max_digits=6,
                                       decimal_places=2,
                                       null=True,
                                       blank=True)
