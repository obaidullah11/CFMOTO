# Generated by Django 4.1.7 on 2023-10-18 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0011_alter_maintenance_list_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="ServiceImage",
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
                (
                    "image1",
                    models.ImageField(
                        blank=True, null=True, upload_to="service_images/"
                    ),
                ),
                (
                    "image2",
                    models.ImageField(
                        blank=True, null=True, upload_to="service_images/"
                    ),
                ),
                (
                    "image3",
                    models.ImageField(
                        blank=True, null=True, upload_to="service_images/"
                    ),
                ),
                (
                    "image4",
                    models.ImageField(
                        blank=True, null=True, upload_to="service_images/"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
