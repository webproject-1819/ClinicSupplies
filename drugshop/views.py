# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse


def home(request):
    # getting our template
    template = loader.get_template('home.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())

def catalogue(request):
    # getting our template
    template = loader.get_template('catalogue.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())

def sales(request):
    # getting our template
    template = loader.get_template('sales.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())

def information(request):
    # getting our template
    template = loader.get_template('information.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())

def shopping_cart(request):
    # getting our template
    template = loader.get_template('shopping_cart.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())


