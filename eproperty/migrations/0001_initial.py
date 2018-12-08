# Generated by Django 2.1.3 on 2018-12-08 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('adv_ID', models.AutoField(primary_key=True, serialize=False)),
                ('advStartDate', models.DateField()),
                ('advEndDate', models.DateField()),
                ('advDescription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('cityID', models.AutoField(primary_key=True, serialize=False)),
                ('cityName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('countryID', models.AutoField(primary_key=True, serialize=False)),
                ('countryName', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Password',
            fields=[
                ('password_ID', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=200)),
                ('encryptedPassword', models.CharField(max_length=200)),
                ('salt', models.CharField(max_length=200)),
                ('userAccountExpiryDate', models.DateField()),
                ('passwordMustChanged', models.BooleanField(default=False)),
                ('passwordReset', models.BooleanField(default=True)),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PermissionType',
            fields=[
                ('permission_ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('propertyID', models.AutoField(primary_key=True, serialize=False)),
                ('propertyTitle', models.CharField(max_length=255)),
                ('propertyStreet', models.CharField(max_length=255)),
                ('propertyPostalCode', models.CharField(max_length=255)),
                ('propertyStreetnumber', models.CharField(max_length=255)),
                ('propertyConstructionDate', models.DateField()),
                ('propertyRegistrationDate', models.DateField()),
                ('propertyNoofHalls', models.IntegerField()),
                ('propertyNumberofRooms', models.IntegerField()),
                ('propertyNoofBathrooms', models.FloatField()),
                ('propertyNoofFloors', models.IntegerField()),
                ('propertyTotalArea', models.FloatField()),
                ('propertyAskingPrice', models.FloatField()),
                ('propertySellingPrice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Property_Facing',
            fields=[
                ('propertyFacing', models.AutoField(primary_key=True, serialize=False)),
                ('propertyFacingName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Property_Sector',
            fields=[
                ('propertySector', models.AutoField(primary_key=True, serialize=False)),
                ('propertySectorName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyCategory',
            fields=[
                ('propertyCategory', models.AutoField(primary_key=True, serialize=False)),
                ('propertyCategoryName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('propertyImageID', models.AutoField(primary_key=True, serialize=False)),
                ('propertyImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('propertyImageDescription', models.TextField()),
                ('propertyID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eproperty.Property')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('provinceID', models.AutoField(primary_key=True, serialize=False)),
                ('provinceName', models.TextField()),
                ('countryID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eproperty.Country')),
            ],
        ),
        migrations.CreateModel(
            name='RoleCode',
            fields=[
                ('roleCode_ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('rolePermission_ID', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=200)),
                ('sysFeature', models.CharField(max_length=200)),
                ('permissionType_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eproperty.PermissionType')),
            ],
        ),
        migrations.CreateModel(
            name='RolePermissionDetail',
            fields=[
                ('rolePermissionDetail_ID', models.AutoField(primary_key=True, serialize=False)),
                ('roleCode_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eproperty.RoleCode')),
                ('rolePermission_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eproperty.RolePermission')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('userRole_ID', models.AutoField(primary_key=True, serialize=False)),
                ('dateAssigned', models.DateField()),
                ('roleCode_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eproperty.RoleCode')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_ID', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='userrole',
            name='user_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eproperty.Users'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertyCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eproperty.PropertyCategory'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertyCity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eproperty.City'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertyCountry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eproperty.Country'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertyFacing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eproperty.Property_Facing'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertyProvince',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eproperty.Province'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertySector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eproperty.Property_Sector'),
        ),
        migrations.AddField(
            model_name='password',
            name='user_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eproperty.Users'),
        ),
        migrations.AddField(
            model_name='city',
            name='countryName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eproperty.Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='provinceID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eproperty.Province'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='propertyID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eproperty.Property', unique=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='user_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eproperty.Users'),
        ),
    ]