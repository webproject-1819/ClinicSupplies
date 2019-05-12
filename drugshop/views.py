# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from drugshop.forms import *
from drugshop.models import *


def home(request):
    # getting our template
    template = loader.get_template('home.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())
def api(request):
    # getting our template
    template = loader.get_template('information.html')

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

def sales(request):

    sales = product.objects.all()
    context = {'sales': sales}
    return render(request, 'sales.html', context)


def producte_detail(request, reference):
    datos = get_object_or_404(product, pk=reference)
    comentarios = review.objects.filter(product=datos)
    context = {'datos': datos, 'comentarios': comentarios}
    return render(request, 'producte.html', context)

def create_review(request):
    try:
        review_instance = review.objects.get(user=request.user)
    except review.DoesNotExist:
        review_instance = review(user=request.user)
    if request.method == 'POST':
        form = reviewForm(request.POST or None, request.FILES, instance=review_instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('catalogue'))
        else:
            return HttpResponse('Ya has comentado, no se permite comentar más de una vez')
    else:
        form = reviewForm()
        context = {'form': form,'review_instace': review_instance}
        return render(request, "review_create.html", context)


def create_prod(request):
    if request.method == 'POST':
        form = productForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('catalogue'))
        else:
            return HttpResponse('Ya existe un producto con esa referencia')
    else:
        form = productForm()
        context = {'form': form}
        return render(request, "product_create.html", context)


def producte_delete(request, pk):
    prod = get_object_or_404(product, pk=pk)
    prod.delete()
    return HttpResponseRedirect(reverse('catalogue'))


def product_edit(request, reference):
    prod = get_object_or_404(product, reference=reference)
    if request.method == 'POST':
        form = productForm(request.POST, instance=prod)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.author = request.user
            prod.save()
            return redirect('catalogue')
    else:
        form = productForm(instance=prod)

        context = {'form': form}
        return render(request, "product_create.html", context)


def product_offer(request, reference):
    prod = get_object_or_404(product, reference=reference)

    if request.method == 'POST':
        form = productOffer(request.POST, instance=prod)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.author = request.user
            prod.save()
            return redirect('catalogue')
    else:

        form = productOffer(instance=prod)


        context = {'form': form , 'prod': prod}
        return render(request, "sale_create.html", context)

def ingresar(request):
    if not request.user.is_anonymous:
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render(request, 'noactivo.html')
            else:
                return render(request, 'nousuario.html')
    else:
        formulario = AuthenticationForm()
    context = {'formulario': formulario}
    return render(request, 'ingresar.html', context)

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    context = {'usuario': usuario}
    return render(request, 'privado.html', context)




@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/home')


def usuarios(request):
    usuarios = User.objects.all()
    recetas = review.objects.all()
    context = {'recetas': recetas, 'usuarios':usuarios}
    return render(request, 'reviews_usuarios.html', context)

def usuario_nuevo(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/home')
    else:
        formulario = UserCreationForm()
    context = {'formulario': formulario}
    return render(request, 'nuevousuario.html', context)



