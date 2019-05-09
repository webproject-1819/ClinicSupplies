from django.conf.urls import url
from django.urls import path

from drugshop import views
from .views import *


urlpatterns = [

    url(r'^home/', home, name='home'),
    url(r'^catalogue/', views.productos, name='catalogue'),
    url(r'^producte/(?P<reference>\d+)$', views.receta, name='producte'),
    url(r'^sales/', sales, name='sales'),
    url(r'^information/', information, name='information'),
    url(r'^shopping_cart/', shopping_cart, name='shopping_cart'),

    path('create_prod/', create_prod, name="create_prod"),


]
