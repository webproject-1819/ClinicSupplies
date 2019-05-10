from django.conf.urls import url
from django.urls import path
from django.views.generic import UpdateView

from drugshop import views
from .views import *


urlpatterns = [

    url(r'^home/', home, name='home'),
    url(r'^catalogue/', views.productos, name='catalogue'),
    url(r'^producte/(?P<reference>\d+)$', views.producte_detail, name='producte'),
    url(r'^product_delete/(?P<pk>\d+)/delete/$', views.producte_delete, name='product_delete'),
    url(r'^sales/', sales, name='sales'),
    url(r'^information/', information, name='information'),
    url(r'^shopping_cart/', shopping_cart, name='shopping_cart'),
    url(r'^product_create/', views.create_prod, name="product_create"),
    url(r'^product_edit/(?P<reference>[-\w]+)/edit/$', views.product_edit, name='product_edit'),





]
