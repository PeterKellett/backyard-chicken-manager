from django.db import models

class EggCollection(models.Model):
    """Model used for storing egg collection data"""
    farm_profile = models.ForeignKey(null=False,
                                     blank=False)
    date = models.DateTimeField(null=False,
                                blank=False)
    flock = models.CharField(max_length=25,
                             null=False,
                             blank=False)
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
    weight_total_laid = models.DecimalField(null=False,
                                            blank=False)
    avg_egg_weight = models.DecimalField(null=False,
                                         blank=False)
    qty_saleable = models.IntegerField(null=False,
                                       blank=False)
    egg_collection_notes = models.CharField(max_length=500,
                                            null=False,
                                            blank=False)
    image_url = models.URLField(null=False,
                                blank=False)
    return self.type
