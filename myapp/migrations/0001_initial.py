# Generated by Django 2.1.1 on 2018-10-18 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('cityID', models.IntegerField(primary_key=True, serialize=False)),
                ('cityName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('countryID', models.IntegerField(primary_key=True, serialize=False)),
                ('countryName', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('propertyID', models.IntegerField(primary_key=True, serialize=False)),
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
                ('propertyFacing', models.IntegerField(primary_key=True, serialize=False)),
                ('Norths', models.CharField(max_length=200)),
                ('South', models.CharField(max_length=200)),
                ('East', models.CharField(max_length=200)),
                ('West', models.CharField(max_length=200)),
                ('Other', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Property_Sector',
            fields=[
                ('propertySector', models.IntegerField(primary_key=True, serialize=False)),
                ('Private', models.CharField(max_length=200)),
                ('Residential', models.CharField(max_length=200)),
                ('Commerical', models.CharField(max_length=200)),
                ('Goevernment', models.CharField(max_length=200)),
                ('Rural', models.CharField(max_length=200)),
                ('Other', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyCategory',
            fields=[
                ('propertyCategory', models.IntegerField(primary_key=True, serialize=False)),
                ('Single', models.CharField(max_length=200)),
                ('Attached', models.CharField(max_length=200)),
                ('Town', models.CharField(max_length=200)),
                ('House', models.CharField(max_length=200)),
                ('Appartment', models.CharField(max_length=200)),
                ('Store', models.CharField(max_length=200)),
                ('Farm', models.CharField(max_length=200)),
                ('Factory', models.CharField(max_length=200)),
                ('Mall', models.CharField(max_length=200)),
                ('Building', models.CharField(max_length=200)),
                ('Other', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('propertyImageID', models.IntegerField(primary_key=True, serialize=False)),
                ('propertyImage', models.BinaryField(blank=True)),
                ('propertyImageDescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('provinceID', models.IntegerField(primary_key=True, serialize=False)),
                ('provinceName', models.TextField()),
                ('countryID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Country')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='propertyCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.PropertyCategory'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertyCity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.City'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertyCountry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Country'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertyFacing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Property_Facing'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertyImages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.PropertyImages'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertyProvince',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Province'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertySector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Property_Sector'),
        ),
        migrations.AddField(
            model_name='city',
            name='countryName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='provinceID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Province'),
        ),
    ]
