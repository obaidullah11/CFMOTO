# Generated by Django 4.1.7 on 2023-09-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dealers", "0006_remove_registeredvehicle_received_vehicle_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registeredvehicle",
            name="model_name",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
