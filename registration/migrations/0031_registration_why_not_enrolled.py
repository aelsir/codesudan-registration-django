# Generated by Django 4.0.4 on 2022-08-30 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0030_remove_batch_curriculum_remove_batch_summery_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='why_not_enrolled',
            field=models.CharField(blank=True, choices=[('online', 'أونلاين'), ('offline', 'اوفلاين')], default=False, max_length=25),
        ),
    ]