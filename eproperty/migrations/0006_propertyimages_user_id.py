# Generated by Django 2.1.3 on 2018-12-09 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eproperty', '0005_property_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyimages',
            name='user_ID',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='eproperty.Users'),
            preserve_default=False,
        ),
    ]
