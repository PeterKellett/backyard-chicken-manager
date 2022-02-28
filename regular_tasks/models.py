from django.db import models


class EggCollection(models.Model):
    """Model used for storing egg collection data"""
    # farm_profile = models.ForeignKey(farmprofile.id, related_name=eggcollections)
    date = models.DateTimeField(null=False,
                                blank=False)
    # flock = models.ForeignKey(flocks.id,
    # related_name=flocks)
    qty_egg_trays = models.IntegerField(null=False,
                                        blank=False)
    qty_egg_singles = models.IntegerField(null=False,
                                          blank=False)
    qty_total_eggs_laid = models.IntegerField(null=False,
                                              blank=False)
    qty_eggs_damaged = models.IntegerField(null=False,
                                           blank=False)
    qty_eggs_broken = models.IntegerField(null=False,
                                          blank=False)
    qty_eggs_personal_use = models.IntegerField(null=False,
                                                blank=False)
    qty_eggs_given_free = models.IntegerField(null=False,
                                              blank=False)
    weight_total_eggs_laid = models.DecimalField(max_digits=5,
                                                 decimal_places=2,
                                                 null=False,
                                                 blank=False)
    avg_egg_weight = models.DecimalField(max_digits=5,
                                         decimal_places=2,
                                         null=False,
                                         blank=False)
    qty_saleable_eggs = models.IntegerField(null=False,
                                            blank=False)
    egg_collection_notes = models.CharField(max_length=500,
                                            null=False,
                                            blank=False)
    # image_url = models.URLField(null=False,
    #                             blank=False)


class FeedingTime(models.Model):
    """Model used for storing feeding time data"""
    # farm_profile = models.ForeignKey(farmprofile.id, related_name=eggcollections)
    date = models.DateTimeField(null=False,
                                blank=False)
    # flock = models.ForeignKey(flocks.id,
    # related_name=flocks)
    food_type = models.IntegerField(null=False,
                                        blank=False)
    amount_food_rem = models.IntegerField(null=False,
                                          blank=False)
    amount_food_added = models.IntegerField(null=False,
                                              blank=False)
    amount_water_rem = models.IntegerField(null=False,
                                           blank=False)
    amount_water_added = models.IntegerField(null=False,
                                          blank=False)
    feeding_notes = models.CharField(max_length=500,
                                            null=False,
                                            blank=False)
    image_url = models.URLField(null=False,
                                blank=False)
