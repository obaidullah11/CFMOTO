# Generated by Django 4.1.7 on 2023-08-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrator'), ('Driver', 'Driver')], default='Driver', max_length=150),
        ),
    ]
