# Generated by Django 4.1.7 on 2023-11-29 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_warranty_warranty_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='bulletins_completed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bulletins_image', models.ImageField(blank=True, null=True, upload_to='bullet_images/')),
                ('bulletins_video', models.FileField(null=True, upload_to='bulletins/')),
                ('bulletins_mechanical_note', models.TextField()),
                ('bulletins_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.bulletins')),
            ],
            options={
                'verbose_name': 'Bulletins submit ',
                'verbose_name_plural': 'Bulletins submit',
            },
        ),
    ]
