from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Property(models.Model):
    propertyID = models.IntegerField(primary_key=true, null=False)
    propertyTitle = models.CharField(max_length=255)
    propertyCategory = models.ForeignKey(PropertyCategory)
    propertySector = models.ForeignKey(Property_Sector)
    propertyFacing = models.ForeignKey(Property_facing)
    propertyCountry = models.ForeignKey(Country)
    propertyImages = models.ForeignKey(PropertyImages, on_delete=models.CASCADE())
    propertyProvince = models.ForeignKey(Province)
    propertyCity = models.ForeignKey(City)
    propertyStreet = models.CharField(max_length=255, null=False)
    propertyPostalCode = models.CharField(max_length=255, null=False)
    propertyStreetnumber = models.CharField(max_length=255, null=False)
    propertyConstructionDate = models.DateField(_("Date"))
    propertyRegistrationDate = models.DateField(-("date"))
    propertyNoofHalls = models.IntegerField(null=False)
    propertyNumberofRooms = models.IntegerField(null=False)
    propertyNoofBathrooms = models.FloatField(null=False)
    propertyNoofFloors = models.IntegerField(null=False)
    propertyTotalArea = models.FloatField(null=False)
    propertyAskingPrice = models.FloatField(null=False)
    propertySellingPrice = models.FloatField(null=False)

    class Country(models.Model):
        countryID = models.IntegerField(primary_key=True)
        countryName = models.TextField(unique=True)

    class Province(models.Model):
        provinceID = models.IntegerField(primary_key=True)
        countryID = models.ForeignKey(Country, on_delete=models.DO_NOTHING, )
        provinceName = models.TextField()

    class City(models.Model):
        cityID = models.IntegerField(primary_key=True)
        cityName = provinceName = models.TextField()
        countryName = models.ForeignKey(Country, on_delete=models.DO_NOTHING, )
        provinceID = models.ForeignKey(Province, on_delete=models.DO_NOTHING, )

    class PropertyImages(models.Model):
        propertyID = models.IntegerField(primary_key=True)
        propertyImage = models.BinaryField(blank=True)
        propertyImageID = models.IntegerField(primary_key=True)
        propertyImageDescription = models.TextField()

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


    def __str__(self):
        return self.title