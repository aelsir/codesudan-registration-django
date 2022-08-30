# Generated by Django 4.0.4 on 2022-08-30 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0031_registration_why_not_enrolled'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='basic_edition_details',
            field=models.TextField(default='details'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='batch',
            name='golden_edition_details',
            field=models.TextField(default='details'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='why_not_enrolled',
            field=models.CharField(blank=True, choices=[('phone off', 'التلفون مقفول'), ('busy', 'مشغول'), ('no answer', 'مافي رد'), ('cancelled', 'قفل الخط'), ('will complete soon', 'حا يسجل قريب'), ('misunderstood', 'فهم غلط'), ('next batch', 'الدفعة الجاية'), ('different program', 'برنامج مختلف')], default=False, max_length=25),
        ),
    ]
