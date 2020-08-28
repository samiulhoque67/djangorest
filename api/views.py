from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CountrySerializer,CitySerializer
from .models import *


@api_view(['GET'])
def country_create_view(request):
	country = Country.objects.all().order_by('-id')
	serializer = CountrySerializer(country, many=True)
	return Response(serializer.data)
@api_view(['GET'])
def city_create_view(request):
	city = City.objects.all().order_by('-id')
	serializer = CitySerializer(city, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def city_create_viewbyid(request,pk):
	city = City.objects.all().order_by('-id')
	serializer = CitySerializer(city, many=True)
	return Response(serializer.data)





@api_view(['POST'])
def city_create_new(self,request):
	serializer = CitySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def country_create_new(self,request):
	serializer = CountrySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)