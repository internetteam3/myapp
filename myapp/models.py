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
        return str(self.countryID)+"-"+self.countryName


class Province(models.Model):
    provinceID = models.IntegerField(primary_key=True)
    countryID = models.ForeignKey(Country, on_delete=models.DO_NOTHING, )
    provinceName = models.TextField()

    def __str__(self):
        return str(self.provinceID)+"-"+self.provinceName


class City(models.Model):
    cityID = models.IntegerField(primary_key=True)
    cityName = models.TextField()
    countryName = models.ForeignKey(Country, on_delete=models.DO_NOTHING, )
    provinceID = models.ForeignKey(Province, on_delete=models.DO_NOTHING, )

    def __str__(self):
        return str(self.cityID)+"-"+self.cityName


class PropertyCategory(models.Model):
    propertyCategory = models.IntegerField(primary_key=True)
    propertyCategoryName = models.CharField(max_length=200)

    def __str__(self):
        return str(self.propertyCategory)+"-"+self.propertyCategoryName


class Property_Sector(models.Model):
    propertySector = models.IntegerField(primary_key=True)
    propertySectorName = models.CharField(max_length=200)

    def __str__(self):
        return str(self.propertySector)+"-"+self.propertySectorName



class Property_Facing(models.Model):
    propertyFacing = models.IntegerField(primary_key=True)
    propertyFacingName = models.CharField(max_length=200)

    def __str__(self):
        return str(self.propertyFacing)+"-"+self.propertyFacingName


class Property(models.Model):
    propertyID = models.IntegerField(primary_key=True, null=False)
    propertyTitle = models.CharField(max_length=255)
    propertyCategory = models.ForeignKey(PropertyCategory, on_delete=models.DO_NOTHING)
    propertySector = models.ForeignKey(Property_Sector, on_delete=models.DO_NOTHING)
    propertyFacing = models.ForeignKey(Property_Facing, on_delete=models.DO_NOTHING)
    propertyCountry = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    #propertyImages = models.ForeignKey(PropertyImages, on_delete=models.DO_NOTHING)
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
        return str(self.propertyID)+"-"+self.propertyTitle+" -> Asking Price: "+str(self.propertyAskingPrice)+"$"


class PropertyImages(models.Model):
    propertyImageID = models.IntegerField(primary_key=True)
    propertyID = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    propertyImage = models.ImageField(blank=True, null=True)
    propertyImageDescription = models.TextField()

    def __str__(self):
        return str(self.propertyImageID)+"-"+self.propertyImageDescription

class  Users(models.Model):
    user_ID = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return str(self.user_ID)+"-"+self.firstName+"-"+self.email

class RoleCode(models.Model):
    roleCode_ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.roleCode_ID)+"-"+self.name

class  UserRole(models.Model):
    userRole_ID = models.IntegerField(primary_key=True)
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    roleCode_ID = models.ForeignKey(RoleCode, on_delete=models.CASCADE)
    dateAssigned = models.DateField()

    def __str__(self):
        return str(self.userRole_ID)+"-"+str(self.user_ID)+"-"+str(self.roleCode_ID)

class Password(models.Model):
    password_ID = models.IntegerField(primary_key=True)
    user_ID = models.ForeignKey(Users, on_delete=models.CASCADE)
    userName = models.CharField(max_length=200)
    encryptedPassword = models.CharField(max_length=200)
    salt = models.CharField(max_length=200)
    userAccountExpiryDate = models.DateField()
    passwordMustChanged = models.BooleanField()
    passwordReset = models.BooleanField()

    def __str__(self):
        return self.userName

class PermissionTyoe(models.Model):
    permission_ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RolePermission(models.Model):
    rolePermission_ID = models.IntegerField(primary_key=True)
    roleCode_ID = models.ForeignKey(RoleCode, on_delete=models.CASCADE)
    permissionType_ID = models.ForeignKey(PermissionTyoe, on_delete=models.CASCADE)
    code = models.CharField(max_length=200)
    sysFeature = models.CharField(max_length=200)

    def __str__(self):
        return self.code

class RolePermissionDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    rolePermission_ID = models.ForeignKey(RolePermission,on_delete=models.CASCADE)
    roleCode_ID = models.ForeignKey(RoleCode,on_delete=models.CASCADE)
