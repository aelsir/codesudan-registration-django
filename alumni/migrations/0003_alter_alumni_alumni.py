# Generated by Django 4.0.4 on 2023-02-07 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alumni', '0002_alumni_facebook_url_alumni_framework_alumni_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='alumni',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
