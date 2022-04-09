from django.db import models
from profiles.models import FarmProfile
from flock_management.models import Flocks, Coops
from django.utils.translation import gettext_lazy as _


class Feeds(models.Model):
    """Model used for storing Food data"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Feeds'
    farm_profile = models.ForeignKey(FarmProfile,
                                     null=False,
                                     blank=False,
                                     on_delete=models.CASCADE)
    feed_name = models.CharField(max_length=50,
                                 null=False,
                                 blank=False)
    qty_food = models.DecimalField(max_digits=6,
                                   decimal_places=2,
                                   null=False,
                                   blank=False)

    def __str__(self):
        return self.feed_name


class Disinfectants(models.Model):
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Disinfectants'
    """Model used for storing different disinfectants"""
    disinfectant_name = models.CharField(max_length=40,
                                         null=False,
                                         blank=False)

    def __str__(self):
        return self.disinfectant_name


class EggCollection(models.Model):
    """Model used for storing egg collection data"""
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
    qty_egg_trays = models.IntegerField(null=True,
                                        blank=True)
    qty_egg_singles = models.IntegerField(null=True,
                                          blank=True)
    qty_total_eggs_laid = models.IntegerField(null=True,
                                              blank=True)
    qty_eggs_damaged = models.IntegerField(null=True,
                                           blank=True)
    qty_eggs_broken = models.IntegerField(null=True,
                                          blank=True)
    qty_eggs_personal_use = models.IntegerField(null=True,
                                                blank=True)
    qty_eggs_given_free = models.IntegerField(null=True,
                                              blank=True)
    weight_total_eggs_laid = models.DecimalField(max_digits=5,
                                                 decimal_places=2,
                                                 null=True,
                                                 blank=True)
    avg_egg_weight = models.DecimalField(max_digits=5,
                                         decimal_places=2,
                                         null=True,
                                         blank=True)
    qty_saleable_eggs = models.IntegerField(null=True,
                                            blank=True)
    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")


class FeedingTime(models.Model):
    """Model used for storing feeding time data"""
    farm_profile = models.ForeignKey(FarmProfile,
                                     null=True,
                                     blank=True,
                                     on_delete=models.CASCADE)
    date = models.DateTimeField(null=False,
                                blank=False,
                                verbose_name='date')
    flock = models.ForeignKey(Flocks,
                              null=False,
                              blank=False,
                              on_delete=models.CASCADE)
    feed_type = models.ForeignKey(Feeds,
                                  null=False,
                                  blank=False,
                                  on_delete=models.CASCADE)
    food_total_setup = models.IntegerField(null=True,
                                     blank=True,
                                     verbose_name='Food Total')
    amount_food_rem = models.IntegerField(null=False,
                                          blank=False,
                                          verbose_name='amount of food remaining')
    amount_food_added = models.IntegerField(null=False,
                                            blank=False,
                                            verbose_name='amount of food added')
    water_total_setup = models.IntegerField(null=True,
                                      blank=True,
                                      verbose_name='Water Total')
    amount_water_rem = models.IntegerField(null=False,
                                           blank=False,
                                           verbose_name='amount of water remaining')
    amount_water_added = models.IntegerField(null=False,
                                             blank=False,
                                             verbose_name='amount of water added')
    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")


class CoopCleaning(models.Model):
    """Model used for storing coop cleaning data"""
    coop = models.ForeignKey(Coops,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    date = models.DateTimeField(null=False,
                                blank=False)
    disinfected = models.BooleanField(null=True,
                                      blank=True)
    disinfectant = models.ForeignKey(Disinfectants,
                                     null=True,
                                     blank=True,
                                     on_delete=models.CASCADE)
    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")
