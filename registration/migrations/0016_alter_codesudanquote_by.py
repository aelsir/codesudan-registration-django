# Generated by Django 4.0 on 2022-03-03 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_codesudanquote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesudanquote',
            name='by',
            field=models.CharField(max_length=64),
        ),
    ]
