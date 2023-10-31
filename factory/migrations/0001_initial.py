# Generated by Django 4.1.7 on 2023-07-29 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicles', '0008_vehicle_orderer_email_vehicle_orderer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factory_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='newOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('W', 'Waiting for Receive'), ('P', 'In Process'), ('S', 'Shipped out of the Factory')], default='W', max_length=1)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_dealer_orders', to=settings.AUTH_USER_MODEL)),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.factory_details')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
    ]
