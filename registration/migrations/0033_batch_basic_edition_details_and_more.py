# Generated by Django 4.0.4 on 2022-10-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0032_remove_batch_basic_edition_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='basic_edition_details',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='batch',
            name='golden_edition_details',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
    ]
