# Generated by Django 4.1.7 on 2023-08-03 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0011_delete_vehiclehystory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='image',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='subcategory',
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='vehicles.vehicle')),
            ],
            options={
                'verbose_name_plural': 'Vehicle Images',
            },
        ),
    ]
