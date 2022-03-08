from django.db import models
from profiles .models import FarmProfile, Breed


# Create your models here.
class Coops(models.Model):
    """Model used for storing FarmFlock attributes"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Coops'
    farm_profile = models.ForeignKey(FarmProfile,
                                     null=False,
                                     blank=False,
                                     on_delete=models.CASCADE)
    coop_name = models.CharField(max_length=20,
                                 null=False,
                                 blank=False)


class Flocks(models.Model):
    """Model used for storing FarmFlock attributes"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Flocks'

    farm_profile = models.ForeignKey(FarmProfile,
                                     null=False,
                                     blank=False,
                                     on_delete=models.CASCADE,
                                     related_name='flocks')
    flock_name = models.CharField(max_length=20,
                                  null=False,
                                  blank=False)
    identifier = models.CharField(max_length=20,
                                  null=True,
                                  blank=True)
    breed = models.ForeignKey(Breed,
                              null=False,
                              blank=False,
                              on_delete=models.CASCADE)
    coop = models.ManyToManyField(Coops)
    hens_qty = models.IntegerField(null=True,
                                   blank=True)
    chicks_qty = models.IntegerField(null=True,
                                     blank=True)
    cocks_qty = models.IntegerField(null=True,
                                    blank=True)
    # def __str__(self):
    #     return self.flock_name
