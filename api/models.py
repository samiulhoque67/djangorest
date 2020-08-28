from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country,null=True, on_delete=models.CASCADE)
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
