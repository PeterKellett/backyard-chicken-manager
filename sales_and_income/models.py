from django.db import models


class RoadsideSales(models.Model):
    """Model used for roadside sales data"""
    # farm_profile = models.ForeignKey(farmprofile.id, related_name=eggcollections)
    date = models.DateTimeField(null=False,
                                blank=False)
    single_egg_price = models.DecimalField(max_digits=5,
                                           decimal_places=2,
                                           null=False,
                                           blank=True)
    half_dozen_eggs_price = models.DecimalField(max_digits=5,
                                                decimal_places=2,
                                                null=False,
                                                blank=True)
    ten_eggs_price = models.DecimalField(max_digits=5,
                                         decimal_places=2,
                                         null=False,
                                         blank=True)
    dozen_eggs_price = models.DecimalField(max_digits=5,
                                           decimal_places=2,
                                           null=False,
                                           blank=True)
    trays_of_eggs_price = models.DecimalField(max_digits=5,
                                               decimal_places=2,
                                               null=False,
                                               blank=True)

    qty_single_eggs_remaining = models.IntegerField(null=False,
                                                blank=True)
    qty_single_eggs_added = models.IntegerField(null=False,
                                            blank=True)
    qty_half_dozen_egg_boxes_remaining = models.IntegerField(null=False,
                                                         blank=True)
    qty_half_dozen_egg_boxes_added = models.IntegerField(null=False,
                                                     blank=True)
    qty_ten_egg_boxes_remaining = models.IntegerField(null=False,
                                                  blank=True)
    qty_ten_egg_boxes_added = models.IntegerField(null=False,
                                              blank=True)
    qty_dozen_egg_boxes_remaining = models.IntegerField(null=False,
                                                    blank=True)
    qty_dozen_egg_boxes_added = models.IntegerField(null=False,
                                                blank=True)
    qty_trays_of_eggs_remaining = models.IntegerField(null=False,
                                                  blank=True)
    qty_trays_of_eggs_added = models.IntegerField(null=False,
                                              blank=True)
    