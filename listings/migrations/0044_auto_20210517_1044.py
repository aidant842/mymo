# Generated by Django 3.1.6 on 2021-05-17 10:44

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0043_auto_20210514_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentlisting',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salelisting',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rentlisting',
            name='expiration_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 15, 10, 44, 3, 459011), null=True),
        ),
        migrations.AlterField(
            model_name='rentlisting',
            name='premium_expiration',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 16, 10, 44, 3, 459034), null=True),
        ),
        migrations.AlterField(
            model_name='salelisting',
            name='expiration_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 17, 10, 44, 3, 456259), null=True),
        ),
        migrations.AlterField(
            model_name='salelisting',
            name='premium_expiration',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 16, 10, 44, 3, 456285), null=True),
        ),
    ]