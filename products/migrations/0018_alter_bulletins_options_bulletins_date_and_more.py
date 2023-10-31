# Generated by Django 4.1.7 on 2023-10-26 05:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0022_alter_factory_options"),
        ("products", "0017_vincode_bulletins"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bulletins",
            options={"verbose_name": "Bulletins", "verbose_name_plural": "Bulletins"},
        ),
        migrations.AddField(
            model_name="bulletins",
            name="Date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="bulletins",
            name="factoryname",
        ),
        migrations.RemoveField(
            model_name="bulletins",
            name="series",
        ),
        migrations.RemoveField(
            model_name="bulletins",
            name="vincode",
        ),
        migrations.AddField(
            model_name="bulletins",
            name="factoryname",
            field=models.ManyToManyField(to="vehicles.factory"),
        ),
        migrations.AddField(
            model_name="bulletins",
            name="series",
            field=models.ManyToManyField(to="vehicles.series"),
        ),
        migrations.AddField(
            model_name="bulletins",
            name="vincode",
            field=models.ManyToManyField(to="products.vincode"),
        ),
    ]
