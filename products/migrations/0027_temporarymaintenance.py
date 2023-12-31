# Generated by Django 4.1.7 on 2023-12-05 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dealers', '0012_remove_registeredvehicle_received_vehicle'),
        ('products', '0026_remove_temporaryrepairing_repairing_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='temporarymaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('executed', models.BooleanField(default=False)),
                ('fill', models.CharField(blank=True, max_length=50, null=True)),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('name', models.CharField(max_length=100)),
                ('time_spent', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tempservices', to='dealers.registeredvehicle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tempuserservices', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
