# Generated by Django 4.1.7 on 2023-08-02 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0008_vehicle_orderer_email_vehicle_orderer_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lights',
            options={'verbose_name_plural': 'Lights'},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name_plural': 'Series'},
        ),
        migrations.AlterModelOptions(
            name='sku',
            options={'verbose_name_plural': 'SKU'},
        ),
        migrations.AlterModelOptions(
            name='vehiclehystory',
            options={'verbose_name_plural': 'Vehicle History'},
        ),
        migrations.AlterModelOptions(
            name='wheels',
            options={'verbose_name_plural': 'Wheels'},
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='body_type',
        ),
        migrations.DeleteModel(
            name='BodyType',
        ),
    ]
