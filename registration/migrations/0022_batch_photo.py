# Generated by Django 4.0.4 on 2022-07-16 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0021_batch_summery'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]