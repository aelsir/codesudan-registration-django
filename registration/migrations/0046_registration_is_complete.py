# Generated by Django 4.0.4 on 2023-02-07 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0045_alter_registration_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]