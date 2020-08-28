from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

 path('country/',views.country_create_view,name='country'),
 path('addcountry/',views.country_create_new,name='addcountry'),
 path('city/',views.city_create_view,name='city'),
 path('addcity/',views.city_create_new,name='addcity'),
]