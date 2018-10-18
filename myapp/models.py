from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Country(models.Model):
    countryID = models.IntegerField(primary_key=True)
    countryName = models.TextField(unique=True)

class Province(models.Model):
    provinceID = models.IntegerField(primary_key=True)
    countryID = models.ForeignKey(Country, on_delete=models.DO_NOTHING, )
    provinceName = models.TextField()

class City(models.Model):
    cityID = models.IntegerField(primary_key=True)
    cityName = models.TextField()
    countryName = models.ForeignKey(Country, on_delete=models.DO_NOTHING, )
    provinceID = models.ForeignKey(Province, on_delete=models.DO_NOTHING, )

class PropertyCategory(models.Model):
    propertyCategory = models.IntegerField(primary_key=True)
    Single = models.CharField(max_length=200)
    House = models.CharField(max_length=200)
    Attached = models.CharField(max_length=200)
    House = models.CharField(max_length=200)
    Town = models.CharField(max_length=200)
    House = models.CharField(max_length=200)
    Appartment = models.CharField(max_length=200)
    Store = models.CharField(max_length=200)
    Farm = models.CharField(max_length=200)
    Factory = models.CharField(max_length=200)
    Mall = models.CharField(max_length=200)
    Building = models.CharField(max_length=200)
    Other = models.CharField(max_length=200)
class Property_Sector(models.Model):
    propertySector = models.IntegerField(primary_key=True)
    Private = models.CharField(max_length=200)
    Residential = models.CharField(max_length=200)
    Commerical = models.CharField(max_length=200)
    Goevernment = models.CharField(max_length=200)
    Rural = models.CharField(max_length=200)
    Other = models.CharField(max_length=200)


class Property_Facing(models.Model):
    propertyFacing = models.IntegerField(primary_key=True)
    North = models.CharField(max_length=200)
    South = models.CharField(max_length=200)
    East = models.CharField(max_length=200)
    West = models.CharField(max_length=200)
    Other = models.CharField(max_length=200)
class PropertyImages(models.Model):
    propertyImageID = models.IntegerField(primary_key=True)
    #propertyID = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    propertyImage = models.BinaryField(blank=True)
    propertyImageDescription = models.TextField()
class Property(models.Model):
    propertyID = models.IntegerField(primary_key=True, null=False)
    propertyTitle = models.CharField(max_length=255)
    propertyCategory = models.ForeignKey(PropertyCategory, on_delete=models.DO_NOTHING)
    propertySector = models.ForeignKey(Property_Sector, on_delete=models.DO_NOTHING)
    propertyFacing = models.ForeignKey(Property_Facing, on_delete=models.DO_NOTHING)
    propertyCountry = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    propertyImages = models.ForeignKey(PropertyImages, on_delete=models.DO_NOTHING)
    propertyProvince = models.ForeignKey(Province, on_delete=models.DO_NOTHING)
    propertyCity = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    propertyStreet = models.CharField(max_length=255, null=False)
    propertyPostalCode = models.CharField(max_length=255, null=False)
    propertyStreetnumber = models.CharField(max_length=255, null=False)
    propertyConstructionDate = models.DateField()
    propertyRegistrationDate = models.DateField()
    propertyNoofHalls = models.IntegerField(null=False)
    propertyNumberofRooms = models.IntegerField(null=False)
    propertyNoofBathrooms = models.FloatField(null=False)
    propertyNoofFloors = models.IntegerField(null=False)
    propertyTotalArea = models.FloatField(null=False)
    propertyAskingPrice = models.FloatField(null=False)
    propertySellingPrice = models.FloatField(null=False)




    def __str__(self):
        return self.title