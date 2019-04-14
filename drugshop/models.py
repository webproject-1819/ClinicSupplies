# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class product(models.Model):

    reference = models.BigIntegerField(primary_key=True, default=00000000000)
    preu = models.FloatField(null=True)
    descripcio = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'images/', default = 'images/None/no-img.jpg')

    def __unicode__(self):
        return u"%s" % self.name


class stock(models.Model):
    key = models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    quantitiy = models.IntegerField(null=True)

    def available(self):
        if stock.objects.filter(product.reference == self.key) and stock.quantitiy >= 1:
            return True

    def __unicode__(self):
        return u"%s" % self.name


class customer(models.Model):
    nom = models.CharField(max_length=255)
    adressa_fisica = models.TextField()
    telefon = models.IntegerField()
    numero_compte = models.BigIntegerField()


class carret(models.Model):
    client = models.ForeignKey(customer,on_delete=models.CASCADE, null=True)
    list = models.ForeignKey(product)

    def final_price(self):
        return self.list.aggregate('preu')





