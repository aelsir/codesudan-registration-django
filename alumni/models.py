from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

LANGUAGES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('java', 'Java'),
        ('csharp', 'C#'),
        ('ruby', 'Ruby'),
    ]

FRAMEWORKS = [
        ('django', 'Django'),
        ('rails', 'Ruby on Rails'),
        ('express', 'Express'),
        ('spring', 'Spring'),
        ('flask', 'Flask'),
    ]
class Alumni(models.Model):
    alumni = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    language = models.CharField(choices=LANGUAGES, max_length=64)
    framework = models.CharField(choices=FRAMEWORKS, max_length=64)
    facebook_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    whatsapp_number = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.alumni.first_name} {self.alumni.father_name}"
    


