from rest_framework import serializers
from .models import Person, City,Upazila,Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields='_all_'
class CitySerializer(serializers.ModelSerializer):    
    country = CountrySerializer(many=True,read_only=True) 
    class Meta:        
        model = City  

        
        fields = ('country','name')