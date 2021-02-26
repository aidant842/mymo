# Generated by Django 3.1.6 on 2021-02-26 11:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_auto_20210225_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentlisting',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='rentlisting',
            name='premium_expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salelisting',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='salelisting',
            name='premium_expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
