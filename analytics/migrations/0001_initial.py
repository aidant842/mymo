# Generated by Django 3.1.6 on 2021-04-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListingAnalytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_listing_views', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
