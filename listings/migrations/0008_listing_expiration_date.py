# Generated by Django 3.1.6 on 2021-02-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20210222_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='expiration_date',
            field=models.DateTimeField(null=True),
        ),
    ]
