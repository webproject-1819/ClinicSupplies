# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.sites import requests
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from drugshop.models import *


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


def productos(request):
    prod = product.objects.all()
    context = {'datos': prod}
    return render(request, 'catalogue.html', context)

def receta(request, reference):
    datos = get_object_or_404(product, pk=reference)
    comentarios = Review.objects.filter(product=datos)
    context = {'datos': datos, 'comentarios': comentarios}
    return render(request, 'producte.html', context)


def create_prod(request):
    if request.method == 'POST':
        form = create_prod(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('catalogue')
    else:
        form = create_prod()
        return render(request, "form.html", {'form': form})
