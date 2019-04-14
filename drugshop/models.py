# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
from django.urls import reverse


class product(models.Model):

    reference = models.BigIntegerField(primary_key=True, default=00000000000)
    preu = models.FloatField(null=True)
    descripcio = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', default='images/None/no-img.jpg')

    def averageRating(self):
        reviewCount = self.product_review_set.count()
        if not reviewCount:
            return 0
        else:
            ratingSum = sum([float(review.rating) for review in self.product_review_set.all()])
            return ratingSum / reviewCount

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('drugshop:product_detail', kwargs={'pk': self.pk})


class stock(models.Model):
    key = models.ForeignKey(product, on_delete=models.CASCADE, null=True, unique=True)
    quantitiy = models.IntegerField(null=True)

    def available(self):
        if stock.objects.filter(product.reference == self.key) and stock.quantitiy >= 1:
            return True

    def __unicode__(self):
        return u"%s" % self.name


class Category(models.Model):
    CATEGORY_CHOICES = ((0, 'Sales'), (1, 'Outlete'), (2, 'New'), (3, 'Standard'))
    category = models.PositiveSmallIntegerField('Category', blank=False, default=0, choices=CATEGORY_CHOICES)
    user = models.ForeignKey(User, default=1)


class Review(models.Model):
    ''' Review atributes '''
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)


class product_review(Review):
    product = models.ForeignKey(product)


class customer(models.Model):
    nom = models.CharField(max_length=255)
    adresa_fisica = models.CharField(max_length=255,default= 'Here')
    telefon = models.IntegerField()
    numero_compte = models.BigIntegerField()
    user = models.ForeignKey(User, default=1, primary_key=True)
