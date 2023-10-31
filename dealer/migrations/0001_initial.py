# Generated by Django 4.1.7 on 2023-07-30 09:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0008_vehicle_orderer_email_vehicle_orderer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='newreceivedvehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('vin_code', models.CharField(blank=True, max_length=17, null=True)),
                ('status', models.CharField(choices=[('PN', 'pending'), ('RC', 'received'), ('AR', 'Assign registration number'), ('DU', 'delivered to user')], default='PN', max_length=2)),
                ('name_received_product', models.CharField(max_length=100)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
    ]