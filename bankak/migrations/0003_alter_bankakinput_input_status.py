# Generated by Django 4.0.4 on 2022-10-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankak', '0002_alter_bankakinput_input_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankakinput',
            name='input_status',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]