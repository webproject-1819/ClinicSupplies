# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
