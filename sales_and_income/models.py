from django.db import models
from profiles.models import FarmProfile
from flock_management.models import Flocks, Coops
from django.utils.translation import gettext_lazy as _


class EggRoadsideSales(models.Model):
    """Model used for roadside sales data"""
    # farm_profile = models.ForeignKey(FarmProfile,
    #                                  blank=False,
    #                                  null=False,
    #                                  on_delete=models.CASCADE)
    #                                 #  related_name='farmprofile')
    date = models.DateTimeField(null=False,
                                blank=False)
    single_egg_price = models.DecimalField(max_digits=5,
                                           decimal_places=2,
                                           null=True,
                                           blank=True)
    half_dozen_eggs_price = models.DecimalField(max_digits=5,
                                                decimal_places=2,
                                                null=True,
                                                blank=True)
    ten_eggs_price = models.DecimalField(max_digits=5,
                                         decimal_places=2,
                                         null=True,
                                         blank=True)
    dozen_eggs_price = models.DecimalField(max_digits=5,
                                           decimal_places=2,
                                           null=True,
                                           blank=True)
    trays_of_eggs_price = models.DecimalField(max_digits=5,
                                              decimal_places=2,
                                              null=True,
                                              blank=True)

    qty_single_eggs_remaining = models.IntegerField(null=True,
                                                    blank=True)
    qty_single_eggs_added = models.IntegerField(null=True,
                                                blank=True)
    qty_half_dozen_egg_boxes_remaining = models.IntegerField(null=True,
                                                             blank=True)
    qty_half_dozen_egg_boxes_added = models.IntegerField(null=True,
                                                         blank=True)
    qty_ten_egg_boxes_remaining = models.IntegerField(null=True,
                                                      blank=True)
    qty_ten_egg_boxes_added = models.IntegerField(null=True,
                                                  blank=True)
    qty_dozen_egg_boxes_remaining = models.IntegerField(null=True,
                                                        blank=True)
    qty_dozen_egg_boxes_added = models.IntegerField(null=True,
                                                    blank=True)
    qty_trays_of_eggs_remaining = models.IntegerField(null=True,
                                                      blank=True)
    qty_trays_of_eggs_added = models.IntegerField(null=True,
                                                  blank=True)
    amount_paid_eggs_roadside = models.DecimalField(max_digits=7,
                                                    decimal_places=2,
                                                    null=True,
                                                    blank=True)
    # Below temporarily removed as involves a more complex wiring
    # sales_amount_eggs_roadside = models.DecimalField(max_digits=7,
    #                                                  decimal_places=2,
    #                                                  null=True,
    #                                                  blank=True)
    # sales_paid_difference_eggs_roadside = models.DecimalField(max_digits=7,
    #                                                           decimal_places=2,
    #                                                           null=True,
    #                                                           blank=True)

    loses_eggs_roadside = models.IntegerField(null=True,
                                              blank=True)

    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")


class EggCollectionSales(models.Model):
    """Model used for collection egg sales data"""
    # farm_profile = models.ForeignKey(FarmProfile,
    #                                 blank=False,
    #                                 null=False,
    #                                 on_delete=models.CASCADE,
    #                                 related_name='farmprofile')
    date = models.DateTimeField(null=False,
                                blank=False)
    # customer_name_eggs_collection = models.CharField(max_length=250,
    #                                                  default='',
    #                                                  blank=False)
    normal_order_qty_eggs_collection = models.IntegerField(null=True,
                                                           blank=True)
    qty_sold_eggs_collection = models.IntegerField(null=True,
                                                   blank=True)
    qty_given_free_eggs_collection = models.IntegerField(null=True,
                                                         blank=True)
    sale_amount_eggs_collection = models.DecimalField(max_digits=5,
                                      decimal_places=2,
                                      null=True,
                                      blank=True)
    amount_paid_eggs_collection = models.DecimalField(max_digits=5,
                                                      decimal_places=2,
                                                      null=True,
                                                      blank=True)
    balance_owed_eggs_collection = models.DecimalField(max_digits=5,
                                                       decimal_places=2,
                                                       null=True,
                                                       blank=True)
    breakages_and_loses_eggs_collection = models.IntegerField(null=True,
                                                              blank=True)
    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")


class EggDeliverySalesDashboard(models.Model):
    """Model used for collection egg sales data"""
    # farm_profile = models.ForeignKey(FarmProfile,
    #                                 blank=False,
    #                                 null=False,
    #                                 on_delete=models.CASCADE,
    #                                 related_name='farmprofile')
    date = models.DateTimeField(null=False,
                                blank=False)
    breakages_and_loses_eggs_delivery = models.IntegerField(null=False,
                                                            blank=True)
    
    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")


class EggDeliverySales(models.Model):
    """Model used for collection egg sales data"""
    # farm_profile = models.ForeignKey(FarmProfile,
    #                                 blank=False,
    #                                 null=False,
    #                                 on_delete=models.CASCADE,
    #                                 related_name='farmprofile')
    date = models.DateTimeField(null=False,
                                blank=False)
    customer_name_eggs_delivery = models.CharField(max_length=250,
                                                   null=True,
                                                   blank=True)
    normal_order_qty_eggs_delivery = models.IntegerField(null=True,
                                                         blank=True)
    delivery_due_date = models.DateTimeField(null=True,
                                             blank=True)
    delivery_not_made = models.BooleanField(null=True,
                                            blank=True)
    delivery_not_made_reason = models.CharField(max_length=250,
                                                null=True,
                                                blank=True)
    qty_sold_eggs_delivery = models.IntegerField(null=True,
                                                 blank=True)
    qty_given_free_eggs_delivery = models.IntegerField(null=True,
                                                       blank=True)
    sale_amount_eggs_delivery = models.DecimalField(max_digits=5,
                                      decimal_places=2,
                                      null=True,
                                      blank=True)
    amount_paid_eggs_delivery = models.DecimalField(max_digits=5,
                                                    decimal_places=2,
                                                    null=True,
                                                    blank=True)
    balance_owed_eggs_delivery = models.DecimalField(max_digits=5,
                                                     decimal_places=2,
                                                     null=True,
                                                     blank=True)
    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")


class EggMarketSales(models.Model):
    """Model used for market sales data"""
    # farm_profile = models.ForeignKey(FarmProfile,
    #                                 blank=False,
    #                                 null=False,
    #                                 on_delete=models.CASCADE,
    #                                 related_name='farmprofile')
    date = models.DateTimeField(null=False,
                                blank=False)
    venue_location_eggs_market = models.CharField(max_length=250,
                                                  null=True,
                                                  blank=True)
    single_egg_price = models.DecimalField(max_digits=5,
                                           decimal_places=2,
                                           null=True,
                                           blank=True)
    half_dozen_eggs_price = models.DecimalField(max_digits=5,
                                                decimal_places=2,
                                                null=True,
                                                blank=True)
    ten_eggs_price = models.DecimalField(max_digits=5,
                                         decimal_places=2,
                                         null=True,
                                         blank=True)
    dozen_eggs_price = models.DecimalField(max_digits=5,
                                           decimal_places=2,
                                           null=True,
                                           blank=True)
    trays_of_eggs_price = models.DecimalField(max_digits=5,
                                              decimal_places=2,
                                              null=True,
                                              blank=True)

    qty_single_eggs_sold = models.IntegerField(null=True,
                                               blank=True)
    qty_half_dozen_egg_boxes_sold = models.IntegerField(null=True,
                                                        blank=True)
    qty_ten_egg_boxes_sold = models.IntegerField(null=True,
                                                 blank=True)
    qty_dozen_egg_boxes_sold = models.IntegerField(null=True,
                                                   blank=True)
    qty_trays_of_eggs_sold = models.IntegerField(null=True,
                                                 blank=True)
    amount_paid_eggs_market = models.DecimalField(max_digits=5,
                                                  decimal_places=2,
                                                  null=True,
                                                  blank=True)
    sales_amount_eggs_market = models.DecimalField(max_digits=5,
                                                     decimal_places=2,
                                                     null=True,
                                                     blank=True)
    sales_paid_difference_eggs_market = models.DecimalField(max_digits=5,
                                                              decimal_places=2,
                                                              null=True,
                                                              blank=True)

    loses_eggs_market = models.IntegerField(null=True,
                                            blank=True)
    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")


class Customer(models.Model):
    """Model used for market sales data"""
    # farm_profile = models.ForeignKey(FarmProfile,
    #                                 blank=False,
    #                                 null=False,
    #                                 on_delete=models.CASCADE,
    #                                 related_name='farmprofile')
    # customer_type = models.ForeignKey(CustomerType,
    #                                   blank=False,
    #                                   null=False,
    #                                   on_delete=models.CASCADE,
    #                                   related_name='customertype'
    #                                   )
    customer_name = models.CharField(max_length=250,
                                     null=True,
                                     blank=True)
    address = models.CharField(max_length=250,
                               null=True,
                               blank=True)
    postcode = models.CharField(max_length=250,
                                null=True,
                                blank=True)
    phone = models.IntegerField(null=True,
                                blank=True)
    date_added = models.DateField(null=True,
                                  blank=True,
                                  auto_now_add=True
                                  )
    # status = models.ForeignKey(customerStatus.id,
    #                            blank=False,
    #                            null=False,
    #                            on_delete=models.CASCADE,
    #                            related_name='customerstatus'
    #                            )
    order_qty = models.IntegerField(null=True,
                                    blank=True)
    # Djgonm doesn;t have a day specific field. Can calc day from date
    route_day = models.DateField(null=True,
                                 blank=True)
                                 # dayOfWeek.id)
    route_position = models.IntegerField(null=True,
                                         blank=True)
    single_egg_price = models.DecimalField(max_digits=5,
                                           decimal_places=2,
                                           null=True,
                                           blank=True)
    six_egg_price = models.DecimalField(max_digits=5,
                                        decimal_places=2,
                                        null=True,
                                        blank=True)
    ten_egg_price = models.DecimalField(max_digits=5,
                                        decimal_places=2,
                                        null=True,
                                        blank=True)
    twelve_egg_price = models.DecimalField(max_digits=5,
                                           decimal_places=2,
                                           null=True,
                                           blank=True)
    tray_price = models.DecimalField(max_digits=5,
                                     decimal_places=2,
                                     null=True,
                                     blank=True)
    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")
