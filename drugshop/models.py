# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product(models.Model):

    reference = models.BigIntegerField(primary_key=True, default=00000000000)
    preu = models.IntegerField(null=True)
    descripcio = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s" % self.name


class Stock(models.Model):
    key = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantitiy = models.IntegerField(null=True)

    def available(self):
        if Stock.objects.filter(Product.reference == self.key) and Stock.quantitiy >= 1:
            return

    def __unicode__(self):
        return u"%s" % self.name
