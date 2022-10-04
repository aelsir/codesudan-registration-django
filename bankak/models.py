from email.policy import default
from django.db import models
from django.forms import BooleanField

# Create your models here.

SUDAN_STATES = [
            ("Outside Sudan", "خارج السودان"),
            ("Khartoum", "الخرطوم"),
            ("Omdurman", "امدرمان"),
            ("Bahri", "بحري"),
            ("North Kordofan", "شمال كردفان"),
            ("Northern", "الشمالية"),
            ("Kassala", "كسّلا"),
            ("Blue Nile", "النيل الأزرق"),
            ("North Darfur", "شمال دارفور"),
            ("South Darfur", "جنوب دارفور"),
            ("South Kordofan", "جنوب كردفان"),
            ("Al Jazirah", "الجزيرة"),
            ("White Nile", "النيل الأبيض"),
            ("River Nile", "نهر النيل"),
            ("Red Sea", "البحر الأحمر"),
            ("Al Qadarif", "القضارف"),
            ("Sennar", "سنّار"),
            ("West Darfur", "غرب دارفور"),
            ("Central Darfur", "وسط دارفور"),
            ("East Darfur", "شرق دارفور"),
            ("East Darfur", "غرب كردفان"),
            ]

BOOL_CHOICES = ((True, 'شغال'), (False, 'ما شغال'))

class BankakInput(models.Model):
    input_status = models.BooleanField(choices=BOOL_CHOICES)
    time = models.DateTimeField(auto_now_add=True)
    state = models.CharField(
        max_length=25,
        choices= SUDAN_STATES,
        default= "Khartoum"
    )


class BankakStatus(models.Model):
    current_status = models.BooleanField(choices=BOOL_CHOICES)
