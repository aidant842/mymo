# Generated by Django 3.1.6 on 2021-02-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_auto_20210226_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentlisting',
            name='floor_area_type',
            field=models.CharField(blank=True, default='Square Meters', max_length=256),
        ),
        migrations.AddField(
            model_name='salelisting',
            name='floor_area_type',
            field=models.CharField(blank=True, default='Square Meters', max_length=256),
        ),
    ]
