# Generated by Django 2.1.5 on 2019-02-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ride_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('ride_name',),
            },
        ),
    ]
