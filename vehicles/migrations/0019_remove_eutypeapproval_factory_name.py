# Generated by Django 4.1.7 on 2023-08-09 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0018_remove_modelname_factory_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eutypeapproval",
            name="factory_name",
        ),
    ]
