from rest_framework import serializers
from .models import Person, City,Upazila,Country,Album,Track,BookDetails,Book

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields =('id','name')
class CitySerializer(serializers.ModelSerializer):    
    
    
    class Meta:        
        model = City  
        fields=('country','name')
        
    def to_representation(self, instance):
        self.fields['country'] =  CountrySerializer(read_only=True)
        return super(CitySerializer, self).to_representation(instance)
        
        

class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']



class BookDetailsSerializer(serializers.ModelSerializer):
   summary = serializers.CharField( max_length=23)
   class Meta:
      model = BookDetails
      fields = ('id', 'summary')

class BookSerializer(serializers.ModelSerializer):
   rbook = BookDetailsSerializer(many=True)

   def create(self, validated_data):
      temp_bok_details= validated_data.pop('rbook')
      print(validated_data)

      new_book = Book.objects.create(**validated_data)
      for i in temp_bok_details:
         BookDetails.objects.create(**i,bok=new_book)
      return new_book
   class Meta:
      model = Book
      fields = ('id','rbook', 'title','author')