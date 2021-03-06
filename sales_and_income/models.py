from django.db import models
from profiles.models import FarmProfile
from flock_management.models import Flocks, Coops
from django.utils.translation import gettext_lazy as _


class SalesType(models.Model):
    """Model used for storing different sales types"""
    type = models.CharField(max_length=20,
                            null=False,
                            blank=False)

    def __str__(self):
        return self.type


class Pricing(models.Model):
    """Model used for storing different customer status'"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Pricing'
    farm_profile = models.ForeignKey(FarmProfile,
                                     blank=False,
                                     null=False,
                                     on_delete=models.CASCADE)
    sales_type = models.ForeignKey(SalesType,
                                   blank=False,
                                   null=False,
                                   on_delete=models.CASCADE)
    single_egg_price = models.DecimalField(max_digits=7,
                                           decimal_places=2,
                                           null=True,
                                           blank=True)
    half_dozen_eggs_price = models.DecimalField(max_digits=7,
                                                decimal_places=2,
                                                null=True,
                                                blank=True)
    ten_eggs_price = models.DecimalField(max_digits=7,
                                         decimal_places=2,
                                         null=True,
                                         blank=True)
    dozen_eggs_price = models.DecimalField(max_digits=7,
                                           decimal_places=2,
                                           null=True,
                                           blank=True)
    trays_of_eggs_price = models.DecimalField(max_digits=7,
                                              decimal_places=2,
                                              null=True,
                                              blank=True)


class CustomerStatus(models.Model):
    """Model used for storing different customer status'"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Customer Status'
    status = models.CharField(max_length=20,
                              null=False,
                              blank=False)

    def __str__(self):
        return self.status


class Customer(models.Model):
    """Model used for market sales data"""
    farm_profile = models.ForeignKey(FarmProfile,
                                     blank=False,
                                     null=False,
                                     on_delete=models.CASCADE)
    customer_sales_type = models.ManyToManyField(to=SalesType,
                                                 blank=False
                                                 )
    customer_name = models.CharField(max_length=250,
                                     null=True,
                                     blank=True)
    address = models.CharField(max_length=250,
                               null=True,
                               blank=True)
    postcode = models.CharField(max_length=250,
                                null=True,
                                blank=True)
    phone = models.CharField(max_length=20,
                             null=True,
                             blank=True)
    date_added = models.DateField(null=True,
                                  blank=True,
                                  auto_now_add=True
                                  )
    customer_status = models.ForeignKey(CustomerStatus,
                                        blank=False,
                                        null=False,
                                        on_delete=models.CASCADE,
                                        related_name='customerstatus'
                                        )
    order_qty = models.IntegerField(null=True,
                                    blank=True)
    # Djgonm doesn;t have a day specific field. Can calc day from date
    route_day = models.DateField(null=True,
                                 blank=True)
    route_position = models.IntegerField(null=True,
                                         blank=True)
    order_price = models.DecimalField(max_digits=5,
                                      decimal_places=2,
                                      null=True,
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

    def __str__(self):
        return self.customer_name


class NonDeliveryReason(models.Model):
    """Model used for storing different customer status'"""
    reason = models.CharField(max_length=20,
                              null=False,
                              blank=False)

    def __str__(self):
        return self.reason


class NonCollectionReason(models.Model):
    """Model used for storing different customer status'"""
    reason = models.CharField(max_length=20,
                              null=False,
                              blank=False)

    def __str__(self):
        return self.reason


class DeliveryRouteDay(models.Model):
    """Model used for storing different customer status'"""
    day = models.CharField(max_length=20,
                           null=False,
                           blank=False)

    def __str__(self):
        return self.day


class LastOrderReceivedWithin(models.Model):
    """Model used for storing different customer status'"""
    time_period = models.CharField(max_length=20,
                                   null=False,
                                   blank=False)

    def __str__(self):
        return self.time_period


class NextOrderDueWithin(models.Model):
    """Model used for storing different customer status'"""
    time_period = models.CharField(max_length=20,
                                   null=False,
                                   blank=False)

    def __str__(self):
        return self.time_period


class EggRoadsideSales(models.Model):
    """Model used for roadside sales data"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Egg roadside sales'
    farm_profile = models.ForeignKey(FarmProfile,
                                     blank=False,
                                     null=False,
                                     on_delete=models.CASCADE)
    date = models.DateTimeField(null=False,
                                blank=False)
    qty_single_eggs_remaining = models.IntegerField(null=True,
                                                    blank=True)
    qty_single_eggs_added = models.IntegerField(null=True,
                                                blank=True)
    qty_single_eggs_in_stock = models.IntegerField(null=True,
                                                   blank=True)
    qty_single_eggs_sold = models.IntegerField(null=True,
                                               blank=True)
    qty_half_dozen_egg_boxes_remaining = models.IntegerField(null=True,
                                                             blank=True)
    qty_half_dozen_egg_boxes_added = models.IntegerField(null=True,
                                                         blank=True)
    qty_half_dozen_egg_boxes_in_stock = models.IntegerField(null=True,
                                                            blank=True)
    qty_half_dozen_egg_boxes_sold = models.IntegerField(null=True,
                                                        blank=True)
    qty_ten_egg_boxes_remaining = models.IntegerField(null=True,
                                                      blank=True)
    qty_ten_egg_boxes_added = models.IntegerField(null=True,
                                                  blank=True)
    qty_ten_egg_boxes_in_stock = models.IntegerField(null=True,
                                                     blank=True)
    qty_ten_egg_boxes_sold = models.IntegerField(null=True,
                                                 blank=True)
    qty_dozen_egg_boxes_remaining = models.IntegerField(null=True,
                                                        blank=True)
    qty_dozen_egg_boxes_added = models.IntegerField(null=True,
                                                    blank=True)
    qty_dozen_egg_boxes_in_stock = models.IntegerField(null=True,
                                                       blank=True)
    qty_dozen_egg_boxes_sold = models.IntegerField(null=True,
                                                   blank=True)
    qty_trays_eggs_remaining = models.IntegerField(null=True,
                                                   blank=True)
    qty_trays_eggs_added = models.IntegerField(null=True,
                                               blank=True)
    qty_trays_eggs_in_stock = models.IntegerField(null=True,
                                                  blank=True)
    qty_trays_eggs_sold = models.IntegerField(null=True,
                                              blank=True)
    losses_eggs_roadside = models.IntegerField(null=True,
                                               blank=True)
    income = models.DecimalField(max_digits=7,
                                 decimal_places=2,
                                 null=False,
                                 blank=False)
    pricing = models.ForeignKey(Pricing,
                                blank=False,
                                null=False,
                                on_delete=models.CASCADE)
    # Below temporarily removed as involves a more complex wiring
    income = models.DecimalField(max_digits=7,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    income_deficit = models.DecimalField(max_digits=7,
                                         decimal_places=2,
                                         null=True,
                                         blank=True)
    notes = models.TextField(null=True,
                             blank=True)
    images = models.ImageField(null=True,
                               blank=True,
                               upload_to="images/")


class EggCollectionSales(models.Model):
    """Model used for collection egg sales data"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Egg collection sales'
    farm_profile = models.ForeignKey(FarmProfile,
                                     blank=False,
                                     null=False,
                                     on_delete=models.CASCADE)
    date = models.DateTimeField(null=False,
                                blank=False)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True
                                 )
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
    breakages_and_losses_eggs_collection = models.IntegerField(null=True,
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
