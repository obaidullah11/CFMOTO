# Generated by Django 4.1.7 on 2023-07-30 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='newreceivedvehicle',
            table='dealer_receivedvehicle',
        ),
    ]
