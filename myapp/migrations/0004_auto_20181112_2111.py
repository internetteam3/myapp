# Generated by Django 2.1.2 on 2018-11-13 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20181111_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='passwordMustChanged',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='password',
            name='passwordReset',
            field=models.BooleanField(default=True),
        ),
    ]