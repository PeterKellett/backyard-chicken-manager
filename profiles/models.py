from django.db import models
from customAuth.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Languages(models.Model):
    language = models.CharField(max_length=20,
                                null=False,
                                blank=False)


class Currency(models.Model):
    currency = models.CharField(max_length=20,
                                null=False,
                                blank=False)


class FarmType(models.Model):
    type = models.CharField(max_length=20,
                            null=False,
                            blank=False)

    def __str__(self):
        return self.type


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,
                                  null=False,
                                  blank=False)
    last_name = models.CharField(max_length=20,
                                 null=False,
                                 blank=False)
    city_country = models.CharField(max_length=20,
                                    null=False,
                                    blank=False)

def __str__(self):
    return self.user


class FarmProfile(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=20,
                                 null=False,
                                 blank=False)
    farm_type = models.ForeignKey(FarmType, on_delete=models.PROTECT)
    farm_sales_roadside = models.BooleanField()
    farm_sales_markets = models.BooleanField()
    farm_sales_deliveries = models.BooleanField()
    farm_sales_collections = models.BooleanField()
    eggs_in_stock = models.IntegerField(default=0,
                                        null=False,
                                        blank=False)
    current_balance = models.DecimalField(max_digits=10,
                                          decimal_places=2,
                                          null=False,
                                          default=0)

def __str__(self):
    return self.user.email


@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
