from django.conf.urls import url
from .views import *

app_name = "clinicsupplies"

urlpatterns = [

    url(r'^home/', home, name="home"),
    url(r'^catalogue/', catalogue, name="catalogue"),

]
