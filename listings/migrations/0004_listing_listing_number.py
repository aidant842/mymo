# Generated by Django 3.1.6 on 2021-02-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20210222_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='listing_number',
            field=models.CharField(max_length=32, null=True),
        ),
    ]