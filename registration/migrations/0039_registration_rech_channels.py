# Generated by Django 4.0.4 on 2022-10-14 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0038_alter_student_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='reach_channels',
            field=models.CharField(choices=[('Our Facebook Page', 'صفحتنا على الفيسبوك'), ('Our Instagram Page', 'صفحتنا على إنستغرام'), ('WhatsApp Group', 'قروب وآتس-أب'), ('Other Social Media', 'شبكات تواصل إجتماعي أخرى'), ('Email', 'البريد الإلكتروني'), ('Friend', 'توصية صديق/ة'), ('Other', 'أخرى')], default='Other', max_length=64),
        ),
    ]
