# Generated by Django 3.1.6 on 2021-03-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0022_auto_20210310_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentlisting',
            name='no_of_bedrooms',
            field=models.IntegerField(null=True),
        ),
    ]
