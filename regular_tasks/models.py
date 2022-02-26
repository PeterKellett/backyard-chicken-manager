from django.db import models

class EggCollection(models.Model):
    """Model used for storing egg collection data"""
    """farm_profile = models.ForeignKey(farmprofile.id,
                                     related_name=eggcollections)"""
    date = models.DateTimeField(null=False,
                                blank=False)
    """flock = models.ForeignKey(flocks.id,
                            related_name=flocks)"""
    qty_total_trays = models.IntegerField(null=False,
                                          blank=False)
    qty_total_single = models.IntegerField(null=False,
                                           blank=False)
    qty_total_laid = models.IntegerField(null=False,
                                         blank=False)
    qty_damaged = models.IntegerField(null=False,
                                      blank=False)
    qty_broken = models.IntegerField(null=False,
                                     blank=False)
    qty_personal_use = models.IntegerField(null=False,
                                           blank=False)
    qty_given_free = models.IntegerField(null=False,
                                         blank=False)
    weight_total_laid = models.DecimalField(max_digits=5,
                                            decimal_places=2,
                                            null=False,
                                            blank=False)
    avg_egg_weight = models.DecimalField(max_digits=5,
                                         decimal_places=2,
                                         null=False,
                                         blank=False)
    qty_saleable = models.IntegerField(null=False,
                                       blank=False)
    egg_collection_notes = models.CharField(max_length=500,
                                            null=False,
                                            blank=False)
    image_url = models.URLField(null=False,
                                blank=False)
