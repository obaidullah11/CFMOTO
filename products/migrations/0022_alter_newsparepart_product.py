# Generated by Django 4.1.7 on 2023-10-31 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealers', '0012_remove_registeredvehicle_received_vehicle'),
        ('products', '0021_bulletins_years_alter_bulletins_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsparepart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealers.registeredvehicle'),
        ),
    ]