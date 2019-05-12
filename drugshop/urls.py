from django.conf.urls import url
from django.urls import path
from django.views.generic import UpdateView

from drugshop import views
from .views import *


urlpatterns = [

    url(r'^home/$', home, name='home'),
    url(r'^$', views.productos, name='catalogue'),
    url(r'^producte/(?P<reference>[-\w]+)$', views.producte_detail, name='producte'),
    url(r'^sales/$', views.sales, name='sales'),
    url(r'^product_delete/(?P<pk>\d+)/delete/$', views.producte_delete, name='product_delete'),
    url(r'^information/$', views.api, name='information'),
    url(r'^shopping_cart/$', shopping_cart, name='shopping_cart'),
    url(r'^product_create/$', views.create_prod, name="product_create"),
    url(r'^product_offer/(?P<reference>[-\w]+)$', views.product_offer, name="product_offer"),
    url(r'^review_create/', views.create_review, name="review_create"),
    url(r'^product_edit/(?P<reference>[-\w]+)/edit/$', views.product_edit, name='product_edit'),

    url(r'^usuarios/$', views.usuarios, name='usuarios'),
    url(r'^usuario/nuevo/$', views.usuario_nuevo, name='usuario_nuevo'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^privado', views.privado, name='privado'),
    url(r'^cerrar/$', views.cerrar, name='cerrar'),


]
