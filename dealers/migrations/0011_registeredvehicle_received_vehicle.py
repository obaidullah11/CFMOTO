# Generated by Django 4.1.7 on 2023-09-23 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dealers", "0010_registeredvehicle_plate_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="registeredvehicle",
            name="received_vehicle",
            field=models.ForeignKey(
                default=9,
                on_delete=django.db.models.deletion.CASCADE,
                to="dealers.receivedvehicle",
            ),
            preserve_default=False,
        ),
    ]