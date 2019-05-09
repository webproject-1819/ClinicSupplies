from django.conf.urls import url
from django.urls import path

from drugshop import views
from .views import *


urlpatterns = [

    url(r'^home/', home, name='home'),
    url(r'^catalogue/', views.productos, name='catalogue'),
    url(r'^producte/(?P<reference>\d+)$', views.producte_detail, name='producte'),
    url(r'^sales/', sales, name='sales'),
    url(r'^information/', information, name='information'),
    url(r'^shopping_cart/', shopping_cart, name='shopping_cart'),

    url(r'^product_create/', views.create_prod, name="product_create"),



]
