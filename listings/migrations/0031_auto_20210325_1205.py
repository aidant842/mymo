# Generated by Django 3.1.6 on 2021-03-25 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0030_auto_20210324_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentlisting',
            name='thumbnail_image',
        ),
        migrations.RemoveField(
            model_name='salelisting',
            name='thumbnail_image',
        ),
    ]
