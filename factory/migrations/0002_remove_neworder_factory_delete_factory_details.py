# Generated by Django 4.1.7 on 2023-07-29 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neworder',
            name='factory',
        ),
        migrations.DeleteModel(
            name='Factory_details',
        ),
    ]