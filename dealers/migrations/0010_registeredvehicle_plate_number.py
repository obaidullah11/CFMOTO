# Generated by Django 4.1.7 on 2023-09-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dealers", "0009_registeredvehicle_vehicle_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="registeredvehicle",
            name="Plate_number",
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
