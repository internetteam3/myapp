# Generated by Django 2.1.3 on 2018-12-12 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eproperty', '0007_remove_propertyimages_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimages',
            name='propertyID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='propImg', to='eproperty.Property'),
        ),
    ]
