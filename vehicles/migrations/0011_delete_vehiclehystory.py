# Generated by Django 4.1.7 on 2023-08-02 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0010_alter_steeringpower_options_vehicle_manufacturer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='vehiclehystory',
        ),
    ]
