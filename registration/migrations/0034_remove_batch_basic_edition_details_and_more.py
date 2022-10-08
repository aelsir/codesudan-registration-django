# Generated by Django 4.0.4 on 2022-10-07 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0033_batch_basic_edition_details_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='basic_edition_details',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='golden_edition_details',
        ),
        migrations.AddField(
            model_name='program',
            name='basic_edition_details',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='program',
            name='golden_edition_details',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
    ]