# Generated by Django 4.1.7 on 2023-08-09 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Garage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiclegarage',
            old_name='orderer_email',
            new_name='user_email',
        ),
        migrations.RenameField(
            model_name='vehiclegarage',
            old_name='orderer_name',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='vehiclegarage',
            old_name='orderer_phone',
            new_name='user_phone',
        ),
    ]
