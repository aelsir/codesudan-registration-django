# Generated by Django 4.0.4 on 2023-01-31 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0007_developer_contribs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='contribs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='followers',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]