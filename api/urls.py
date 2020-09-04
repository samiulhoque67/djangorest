from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'country', views.CountrySet),
router.register(r'city', views.CitySet)

urlpatterns = [
path('', include(router.urls)),
]