from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country,related_name='country',null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
class Upazila(models.Model):

    city=models.ForeignKey(City,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
class Person(models.Model):
    name = models.CharField(max_length=124)
    nid = models.CharField(max_length=50,null=True, unique=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    upazila = models.ForeignKey(Upazila,on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return self.name


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    def __str__(self):
        return self.album_name

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)




class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    def __str__(self):
    	return self.title

class BookDetails(models.Model):
    bok = models.ForeignKey('Book', on_delete=models.CASCADE, related_name="rbook")
    summary = models.CharField(max_length=200) # one book can have multiple summaries

    def __str__(self):
    	return self.summary