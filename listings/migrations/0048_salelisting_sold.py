# Generated by Django 3.1.6 on 2021-05-24 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0047_auto_20210517_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='salelisting',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]