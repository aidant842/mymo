# Generated by Django 3.1.6 on 2021-02-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]