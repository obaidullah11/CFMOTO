# Generated by Django 4.1.7 on 2023-09-23 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dealers", "0011_registeredvehicle_received_vehicle"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="registeredvehicle",
            name="received_vehicle",
        ),
    ]