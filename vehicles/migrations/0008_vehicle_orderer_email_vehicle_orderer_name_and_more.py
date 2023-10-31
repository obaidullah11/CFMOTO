# Generated by Django 4.1.7 on 2023-07-29 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0007_vehiclehystory'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='orderer_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='orderer_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='orderer_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]