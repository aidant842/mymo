# Generated by Django 3.1.6 on 2021-04-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0033_salelisting_email_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentlisting',
            name='email_sent',
            field=models.BooleanField(default=False),
        ),
    ]