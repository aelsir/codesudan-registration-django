# Generated by Django 4.0.4 on 2022-10-04 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankak', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankakinput',
            name='input_status',
            field=models.CharField(choices=[(True, 'Yes'), (False, 'No')], default=True, max_length=25),
        ),
    ]