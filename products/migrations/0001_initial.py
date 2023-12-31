# Generated by Django 4.1.7 on 2023-10-18 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("MODEL_SKU", models.CharField(max_length=50, null=True)),
                ("CATEGORY", models.CharField(max_length=50, null=True)),
                ("MODEL_NAME", models.CharField(max_length=50, null=True)),
                ("FACTORY", models.CharField(max_length=50, null=True)),
                ("SERIES", models.CharField(max_length=50, null=True)),
                ("FACTORY_NAME", models.CharField(max_length=50, null=True)),
                ("COLOR", models.CharField(max_length=50, null=True)),
                ("EU_TYPE", models.CharField(max_length=50, null=True)),
                ("WHEELS", models.CharField(max_length=50, null=True)),
                ("STEERING", models.CharField(max_length=50, null=True)),
                ("SCREEN", models.CharField(max_length=50, null=True)),
                ("LIGHTS", models.CharField(max_length=50, null=True)),
                ("CARGO_COMPARTMENTS", models.CharField(max_length=50, null=True)),
                ("COMMUNICATION_TERMINAL", models.CharField(max_length=50, null=True)),
                ("vehicle_system_id", models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
