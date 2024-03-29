# Generated by Django 3.1.6 on 2021-03-02 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0019_auto_20210301_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentListingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='')),
                ('listing', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='listingImages', to='listings.rentlisting')),
            ],
        ),
    ]
