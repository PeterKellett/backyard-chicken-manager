from django.db import models
from profiles.models import FarmProfile
from flock_management.models import Flocks
from django.utils import timezone


class PaymentMethods(models.Model):
    """Model used for Purchases Categories"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Payment Methods'
    payment_method = models.CharField(max_length=50,
                                       null=True,
                                       blank=True)
    def __str__(self):
        return self.payment_methods


class PurchasesCategory(models.Model):
    """Model used for Purchases Categories"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Purchases Category'
    category = models.CharField(max_length=50,
                                null=True,
                                blank=True)
    def __str__(self):
        return self.category


class Purchases(models.Model):
    """Model used for storing Purchases data"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Purchases'
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
    category = models.ForeignKey(PurchasesCategory,
                                 null=False,
                                 blank=False,
                                 on_delete=models.CASCADE)
    product = models.CharField(max_length=50,
                               null=True,
                               blank=True)
    total_cost = models.DecimalField(max_digits=7,
                                     decimal_places=2,
                                     null=True,
                                     blank=True)
    amount_purchased = models.DecimalField(max_digits=7,
                                           decimal_places=2,
                                           null=True,
                                           blank=True)
    unit_of_measurement = models.CharField(max_length=50,
                                           null=True,
                                           blank=True)
    payment_method = models.CharField(max_length=50,
                                      null=True,
                                      blank=True)
    receipt_reference = models.CharField(max_length=50,
                                         null=True,
                                         blank=True)
    seller_name = models.CharField(max_length=50,
                                   null=True,
                                   blank=True)
    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")
