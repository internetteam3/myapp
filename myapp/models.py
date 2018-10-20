from django.db import models
import datetime
from django.contrib.auth.models import User
from enum import Enum
from django.urls import reverse
from django.utils import timezone


# Create your models here.


class Country(models.Model):
    countryID = models.IntegerField(primary_key=True)
    countryName = models.TextField(unique=True)

    def __str__(self):
        return self.countryName


class Province(models.Model):
    provinceID = models.IntegerField(primary_key=True)
    countryID = models.ForeignKey(Country, on_delete=models.DO_NOTHING, )
    provinceName = models.TextField()

    def __str__(self):
        return self.provinceName


class City(models.Model):
    cityID = models.IntegerField(primary_key=True)
    cityName = models.TextField()
    countryName = models.ForeignKey(Country, on_delete=models.DO_NOTHING, )
    provinceID = models.ForeignKey(Province, on_delete=models.DO_NOTHING, )

    def __str__(self):
        return self.cityName


class PropertyCategory(Enum):
    SingleHouse = "Single House"
    AttachedHouse = "Attached House"
    TownHouse = "Town House"
    Appartment = "Appartment"
    Store = "Store"
    Farm = "Farm"
    Factory = "Factory"
    Mall = "Mall"
    Building = "Building"
    Other = "Other"



class Property_Sector(Enum):
    Private = "Private"
    Residential = "Residential"
    Commerical = "Commercial"
    Government = "Government"
    Rural = "Rural"
    Other = "Other"



class Property_Facing(Enum):
    North = "North"
    South = "South"
    East = "East"
    West = "West"
    Other = "Other"





class Property(models.Model):
    propertyID = models.IntegerField(primary_key=True, null=False)
    propertyTitle = models.CharField(max_length=255)
    propertyCategory = models.CharField(max_length=255, null=False, choices=[(tag.name, tag.value) for tag in PropertyCategory])
    propertySector = models.CharField(max_length=255, null=False, choices=[(tag.name, tag.value) for tag in Property_Sector])
    propertyFacing = models.CharField(max_length=255, null=False, choices=[(tag.name, tag.value) for tag in Property_Facing])
    propertyCountry = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    # propertyImages = models.ForeignKey(PropertyImages, on_delete=models.DO_NOTHING)
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
        return self.propertyTitle



class PropertyImages(models.Model):
    propertyImageID = models.IntegerField(primary_key=True)
    propertyID = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    propertyImage = models.ImageField(blank=True, null=True)
    propertyImageDescription = models.TextField()

    def __str__(self):
        return self.propertyImageDescription
