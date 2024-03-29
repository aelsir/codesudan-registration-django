# Generated by Django 4.0.4 on 2022-08-02 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0027_registration_is_texted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='is_enroll',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='is_phoned',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='is_texted',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='package',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
