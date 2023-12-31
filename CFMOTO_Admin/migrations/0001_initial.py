# Generated by Django 4.1.7 on 2023-08-09 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Garage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApproveAdminVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('approved', 'Approved by Admin'), ('not_approved', 'Not Approved by Admin')], default='not_approved', max_length=20)),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle_garage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Garage.vehiclegarage')),
            ],
        ),
    ]
