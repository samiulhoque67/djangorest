from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CountrySerializer,CitySerializer,AlbumSerializer,BookDetailsSerializer,BookSerializer
from .models import *
from rest_framework.views import APIView
from rest_framework import viewsets


class CountrySet(viewsets.ModelViewSet):
	queryset=Country.objects.all()
	serializer_class=CountrySerializer
class CitySet(viewsets.ModelViewSet):
	queryset=City.objects.all()
	serializer_class=CitySerializer


"""
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


@api_view(['GET'])
def album_create_view(request):
	album = Album.objects.all().order_by('-id')
	serializer =AlbumSerializer(album, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def book_create_view(request):
	book = Book.objects.all().order_by('-id')
	serializer =BookSerializer(book, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def book_create_new(request):
	serializer = BookSerializer(data=request.data)
	print(serializer)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	return Response(serializer.errors)




@api_view(['POST'])
def city_create_new(request):
	
	serializer = CitySerializer(data=request.data)
	
	

	if serializer.is_valid():
		print(serializer)
		serializer.save()
		return Response(serializer.data)


@api_view(['POST'])
def country_create_new(request):
	serializer = CountrySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	return Response(serializer.errors)
"""