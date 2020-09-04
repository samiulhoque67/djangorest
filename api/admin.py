from django.contrib import admin

# Register your models here.
from .models import City, Country,Upazila,Album,Track,Book,BookDetails

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Upazila)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Book)
admin.site.register(BookDetails)

