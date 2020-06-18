from django.conf import settings
from django.db import models


class Equipment(models.Model):
    description = models.CharField(max_length=30)
    identification = models.CharField(max_length=30)
    min_acceptation = models.DecimalField(max_digits=7, decimal_places=3)
    max_acceptation = models.DecimalField(max_digits=7, decimal_places=3)
    status = models.BooleanField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)


class Weight(models.Model):
    stable = models.BooleanField()
    gross_weight = models.DecimalField(max_digits=7, decimal_places=3)
    tare = models.DecimalField(max_digits=7, decimal_places=3)
    net_weight = models.DecimalField(max_digits=7, decimal_places=3)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)


class Charge(models.Model):
    identification = models.CharField(max_length=30)
    weight = models.ForeignKey(Weight, on_delete=models.PROTECT)
    equipment = models.ForeignKey(Equipment, on_delete=models.PROTECT)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
