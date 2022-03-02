from django.db import models


class EggRoadsideSales(models.Model):
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
    amount_paid_eggs_roadside = models.DecimalField(max_digits=5,
                                                    decimal_places=2,
                                                    null=False,
                                                    blank=True)
    sales_amount_eggs_roadside = models.DecimalField(max_digits=5,
                                                     decimal_places=2,
                                                     null=False,
                                                     blank=True)
    sales_paid_difference_eggs_roadside = models.DecimalField(max_digits=5,
                                                              decimal_places=2,
                                                              null=False,
                                                              blank=True)

    loses_eggs_roadside = models.IntegerField(null=False,
                                              blank=True)


class EggCollectionSales(models.Model):
    """Model used for collection egg sales data"""
    # farm_profile = models.ForeignKey(farmprofile.id, related_name=eggcollections)
    date = models.DateTimeField(null=False,
                                blank=False)
    customer_name_eggs_collection = models.CharField(max_length=250,
                                                     null=False,
                                                     blank=False)
    normal_order_qty_eggs_collection = models.IntegerField(null=False,
                                                           blank=True)
    qty_sold_eggs_collection = models.IntegerField(null=False,
                                                   blank=False)
    qty_given_free_eggs_collection = models.IntegerField(null=False,
                                                         blank=True)
    amount_paid_eggs_collection = models.DecimalField(max_digits=5,
                                                      decimal_places=2,
                                                      null=False,
                                                      blank=True)
    balance_owed_eggs_collection = models.DecimalField(max_digits=5,
                                                       decimal_places=2,
                                                       null=False,
                                                       blank=True)
    breakages_and_loses_eggs_collection = models.IntegerField(null=False,
                                                              blank=True)


class EggDeliverySales(models.Model):
    """Model used for collection egg sales data"""
    # farm_profile = models.ForeignKey(farmprofile.id, related_name=eggcollections)
    date = models.DateTimeField(null=False,
                                blank=False)
    customer_name_eggs_delivery = models.CharField(max_length=250,
                                                   null=False,
                                                   blank=False)
    normal_order_qty_eggs_delivery = models.IntegerField(null=False,
                                                         blank=True)
    delivery_due_date = models.DateTimeField(null=False,
                                             blank=False)
    delivery_not_made = models.BooleanField(null=False,
                                            blank=True)
    delivery_not_made_reason = models.CharField(max_length=250,
                                                null=False,
                                                blank=False)
    qty_sold_eggs_delivery = models.IntegerField(null=False,
                                                 blank=False)
    qty_given_free_eggs_delivery = models.IntegerField(null=False,
                                                       blank=True)
    amount_paid_eggs_delivery = models.DecimalField(max_digits=5,
                                                    decimal_places=2,
                                                    null=False,
                                                    blank=True)
    balance_owed_eggs_delivery = models.DecimalField(max_digits=5,
                                                     decimal_places=2,
                                                     null=False,
                                                     blank=True)
    breakages_and_loses_eggs_delivery = models.IntegerField(null=False,
                                                            blank=True)


class EggMarketSales(models.Model):
    """Model used for market sales data"""
    # farm_profile = models.ForeignKey(farmprofile.id, related_name=eggcollections)
    date = models.DateTimeField(null=False,
                                blank=False)
    venue_location_eggs_market = models.CharField(max_length=250,
                                                  null=False,
                                                  blank=True)
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

    qty_single_eggs_sold = models.IntegerField(null=False,
                                               blank=True)
    qty_half_dozen_egg_boxes_sold = models.IntegerField(null=False,
                                                        blank=True)
    qty_ten_egg_boxes_sold = models.IntegerField(null=False,
                                                 blank=True)
    qty_dozen_egg_boxes_sold = models.IntegerField(null=False,
                                                   blank=True)
    qty_trays_of_eggs_sold = models.IntegerField(null=False,
                                                 blank=True)
    amount_paid_eggs_market = models.DecimalField(max_digits=5,
                                                  decimal_places=2,
                                                  null=False,
                                                  blank=True)
    sales_amount_eggs_roadside = models.DecimalField(max_digits=5,
                                                     decimal_places=2,
                                                     null=False,
                                                     blank=True)
    sales_paid_difference_eggs_roadside = models.DecimalField(max_digits=5,
                                                              decimal_places=2,
                                                              null=False,
                                                              blank=True)

    loses_eggs_market = models.IntegerField(null=False,
                                            blank=True)


