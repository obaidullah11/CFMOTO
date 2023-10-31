# Generated by Django 4.1.7 on 2023-08-09 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0019_remove_eutypeapproval_factory_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="eutypeapproval",
            name="factory_name",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Factory_eutype",
                to="vehicles.factory",
            ),
        ),
    ]
