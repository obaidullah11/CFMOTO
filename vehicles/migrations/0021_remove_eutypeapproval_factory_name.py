# Generated by Django 4.1.7 on 2023-08-09 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0020_eutypeapproval_factory_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eutypeapproval",
            name="factory_name",
        ),
    ]