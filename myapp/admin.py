from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Property, PropertyCategory, Property_Sector, Property_Facing,PropertyImages, Country, Province, City
# Register your models here.
admin.site.register(Property)
admin.site.register(PropertyImages)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)