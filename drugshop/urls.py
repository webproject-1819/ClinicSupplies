from django.conf.urls import url
from .views import *

app_name = "clinicsupplies"

urlpatterns = [

    url(r'^home/', home, name="home"),
    url(r'^catalogue/', catalogue, name="catalogue"),
    url(r'^sales/', catalogue, name="sales"),
    url(r'^information/', catalogue, name="information"),
    url(r'^shopping_cart/', catalogue, name="shopping_cart"),
]
