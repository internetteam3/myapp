from django.db import models
import datetime
from django.contrib.auth.models import User
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


class PropertyCategory(models.Model):
    propertyCategory = models.IntegerField(primary_key=True)
    SingleHouse = models.BooleanField(default=True)
    AttachedHouse = models.BooleanField()
    memberName = models.CharField(max_length=200)
    TownHouse = models.BooleanField()
    Appartment = models.BooleanField()
    Store = models.BooleanField()
    Farm = models.BooleanField()
    Factory = models.BooleanField()
    Mall = models.BooleanField()
    Building = models.BooleanField()
    Other = models.CharField(max_length=200)

    def __str__(self):
        return self.propertyCategory


class Property_Sector(models.Model):
    propertySector = models.IntegerField(primary_key=True)
    Private = models.BooleanField(default=True)
    Residential = models.BooleanField()
    Commerical = models.BooleanField()
    Goevernment = models.BooleanField()
    Rural = models.BooleanField()
    Other = models.CharField(max_length=200)

    def __str__(self):
        return self.propertySector


class Property_Facing(models.Model):
    propertyFacing = models.IntegerField(primary_key=True)
    North = models.BooleanField(default=True)
    South = models.BooleanField()
    East = models.BooleanField()
    West = models.BooleanField()
    Other = models.CharField(max_length=200)

    def __str__(self):
        return self.propertyFacing


class PropertyImages(models.Model):
    propertyImageID = models.IntegerField(primary_key=True)
    # propertyID = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    propertyImage = models.ImageField(blank=True, null=True)
    propertyImageDescription = models.TextField()

    def __str__(self):
        return self.propertyImageID


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
        return self.propertyTitle
