# Generated by Django 4.0.4 on 2022-07-24 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0024_registration_batch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='photo',
        ),
    ]
