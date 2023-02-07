from email.policy import default
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.contrib.postgres.fields import ArrayField


UNIVERSITY = (
    ("University of Khartoum", "جامعة الخرطوم"),
    ("Sudan University of Science and Technology", "جامعة السودان للعلوم و التكنلوجيا"),
    ("Omdurman Islamic University", "جامعة أمدرمان الإسلامية"),
    ("Al Neelain University", "جامعة النيلين"),
    ("National Ribat University", "جامعة الرباط الوطني"),
    ("Aljazeera University", "جامعة الجزيرة"),
    ("Ahfad University for Women", "جامعة الأحفاد للبنات"),
    ("Alzaiem Alazhari University", "جامعة الزعيم الأزهري"),
    ("Karary University", "جامعة كرري"),
    ("University of Science and Technology", "جامعة العلوم و التقانة"),
    ("The Future university", "جامعة المستقبل"),
    ("University of Medical Sciences and Technology", "جامعة العلوم الطبية والتكنولوجيا"),
    ("Sudan international University", "جامعة السودان المفتوحة"),
    ("Other", "أخرى"),
)

# Create your models here.
class Student(AbstractUser):
    is_complete = models.BooleanField(null=False, default=False)
    first_name = models.CharField(max_length=64, blank=True, null=True)
    father_name = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    occupation = models.CharField(max_length=64, blank=True, null=True)
    university = models.CharField(
        max_length=64,
        choices= UNIVERSITY,
        default= "Other"
    )
    specialization = models.CharField(max_length=64, blank=True, null=True)
    state = models.CharField(max_length=64 ,blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return(f"{self.first_name} {self.father_name}")



class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name_english = models.CharField(max_length=128, null = False)
    name_arabic = models.CharField(max_length=128, null = False)

    def __str__(self):
        return(self.name_english)


class Program(models.Model):
    id = models.AutoField(primary_key=True)
    name_english = models.CharField(max_length=128, null=False)
    name_arabic = models.CharField(max_length=128, null = False)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    code = models.CharField(max_length=4)
    curriculum = models.TextField()
    summery = models.TextField()
    basic_edition_details = models.TextField()
    golden_edition_details = models.TextField()

    class Meta:
        ordering = ["-track", "-name_english"]

    def __str__(self):
        return(self.name_arabic)


MODE_CHOICES = (
    ("online", "أونلاين"),
    ("offline", "اوفلاين")
)
class Batch(models.Model):
    id=models.AutoField(primary_key=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    number = models.SmallIntegerField()
    starting_at = models.DateField()
    ending_at = models.DateField()
    basic_edition_price = models.IntegerField()
    golden_edition_price = models.IntegerField()
    mode = models.CharField(
        max_length=20,
        choices= MODE_CHOICES,
        default= "online"
    )
    instructor = models.CharField(max_length=64)
    duration_in_weeks = models.SmallIntegerField()
    sessions_per_week = models.SmallIntegerField()
    session_duration_in_hours = models.FloatField()
    whatsapp_url = models.URLField()

    class Meta:
        ordering = ["-program", "-id"]


    def __str__(self):
        return (f"الدفعة {self.number} من {self.program}")


CHANNELS = (
    ("Our Facebook Page", "صفحتنا على الفيسبوك"),
    ("Our Instagram Page", "صفحتنا على إنستغرام"),
    ("WhatsApp Group", "قروب وآتس-أب"),
    ("Other Social Media", "شبكات تواصل إجتماعي أخرى"),
    ("Email", "البريد الإلكتروني"),
    ("Friend", "توصية صديق/ة"),
    ("Intelligent Pattern Page", "صفحة Intelligent Pattern"),
    ("Other", "أخرى"),
    ("Unknown", "غير معروف"),
)
class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='my_registrations')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, default=None)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    package = models.CharField(max_length=64, blank=True)
    price = models.IntegerField(default=0, blank=True)
    is_register = models.BooleanField(default=False)
    is_texted = models.BooleanField(default=False, blank=True)
    transaction_id = models.PositiveBigIntegerField(null=True, default=None, blank=True)
    is_enroll = models.BooleanField(default=False, blank=True)
    is_complete = models.BooleanField(default=False)
    reach_channels = models.CharField(
        max_length=64,
        choices= CHANNELS,
        blank=True,
        null=True,
    )
    
    

    """
    Not need for now because I'm the one managing the whole thing:

    is_phoned = models.BooleanField(default=False, blank=True)
    in_discord = models.BooleanField(default=False, blank=True)
    is_graduated = models.BooleanField(default=False, blank=True)
    is_certificated = models.BooleanField(default=False, blank=True)
    why_not_enrolled = models.CharField(
            max_length=25,
            choices= WHY_NOT_ENROLLED,
            default= False,
            blank=True
        )
    WHY_NOT_ENROLLED = (
        ("phone off", "التلفون مقفول"),
        ("busy", "مشغول"),
        ("no answer", "مافي رد"),
        ("cancelled", "قفل الخط"),
        ("will complete soon", "حا يسجل قريب"),
        ("misunderstood", "فهم غلط"),
        ("next batch", "الدفعة الجاية"),
        ("different program", "برنامج مختلف")
    )
    """
    

    def __str__(self):
        return(f"{self.student.first_name} PN {self.student.username} registerd for {self.program} is_enroll {self.is_enroll}")
class CodeSudanQuote(models.Model):
    id = models.AutoField(primary_key=True)
    quote = models.TextField()
    by = models.CharField(max_length=64)
    
    def __str__(self):
        return(f"{self.quote[:40]}: {self.by}")
