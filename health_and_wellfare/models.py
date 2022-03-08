from django.db import models
from profiles.models import FarmProfile


class Supplements(models.Model):
    """Model used for storing Food data"""
    class Meta:
        """Overwrite the default Django pluralisation"""
        verbose_name_plural = 'Supplements'
    farm_profile = models.ForeignKey(FarmProfile,
                                     null=False,
                                     blank=False,
                                     on_delete=models.CASCADE)
    supplement_name = models.CharField(max_length=50,
                                       null=False,
                                       blank=False)
    qty_supplements = models.DecimalField(max_digits=6,
                                         decimal_places=2,
                                         null=False,
                                         blank=False)
