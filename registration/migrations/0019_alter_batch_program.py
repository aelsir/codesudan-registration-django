# Generated by Django 4.0.4 on 2022-07-15 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_batch_basic_edition_price_batch_curriculum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='program',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.program'),
        ),
    ]
