# Generated by Django 4.1.7 on 2023-07-29 20:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0006_delete_vehiclehystory'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehiclehystory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=200)),
                ('historical_note', models.CharField(choices=[('The vehicle order has been forwarded to the factory.', 'The vehicle order has been forwarded to the factory.'), ('The vehicle is out of production.', 'The vehicle is out of production.'), ('The vehicle is ready for transport from the factory.', 'The vehicle is ready for transport from the factory.'), ('The vehicle arrived at the MOTOHOBI warehouse.', 'The vehicle arrived at the MOTOHOBI warehouse.'), ('The vehicle has been transferred to the dealer.', 'The vehicle has been transferred to the dealer.'), ('The vehicle is registered and issued with a reg number', 'The vehicle is registered and issued with a reg number'), ('The vehicle has been issued to the owner.', 'The vehicle has been issued to the owner.')], max_length=150)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
    ]
