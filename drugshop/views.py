# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from drugshop.forms import productForm, stockForm
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

class product_detail(DetailView):
	model = product
	template_name = '#TODO'

	def get_context_data(self, **kwargs):
		context = super(product_detail, self).get_context_data(**kwargs)
		context['RATING_CHOICES'] = product_review.RATING_CHOICES
		return context


class productCreate(CreateView):
	''' Create Movie, use template form.html '''
	model = product
	template_name = 'form.html'
	form_class = productForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(productCreate, self).form_valid(form)

def productDelete(request, pk):
	'''Movie delete'''
	product1 = get_object_or_404(product, pk=pk)
	product1.delete()
	return HttpResponseRedirect(reverse('drugshop:product_list', ))

class stockCreate(CreateView):
	''' Create Actor, use template form.html '''
	model = stock
	template_name = 'form.html'
	form_class = stockForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(stockCreate, self).form_valid(form)

def ActorDelete(request, pk):
	'''Actor delete'''
	stock1 = get_object_or_404(stock, pk=pk)
	stock1.delete()
	return HttpResponseRedirect(reverse('drugshop:stock_list', ))

def reviewP(request, pk):
	product1 = get_object_or_404(product, pk=pk)
	reviews = product_review(
		rating=request.POST['rating'],
		comment=request.POST['comment'],
		user=request.user,
		product=product1)
	reviews.save()
	return HttpResponseRedirect(reverse('drugshop:product_detail', args=(product1.id,)))



