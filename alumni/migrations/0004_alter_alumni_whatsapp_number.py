# Generated by Django 4.0.4 on 2023-02-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0003_alter_alumni_alumni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='whatsapp_number',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
