# Generated by Django 2.1.3 on 2018-12-08 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eproperty', '0003_auto_20181208_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='passwordMustChanged',
            field=models.BooleanField(default=True),
        ),
    ]