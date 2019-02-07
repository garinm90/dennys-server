# Generated by Django 2.1.5 on 2019-02-07 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ride',
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_rides',
            field=models.ManyToManyField(blank=True, related_name='customers', to='rides.Ride'),
        ),
    ]
