from django.db import models

# Create your models here.

class Developer(models.Model):
    name_arabic = models.CharField(max_length=64)
    name_english = models.CharField(max_length=64)
    rank = models.SmallIntegerField()
    facebook_url = models.URLField()
    linkedin_url = models.URLField()
    github_url = models.URLField()

    class Meta:
        permissions = [
            ('contributor', "add or remove in developer ranking")
        ]

    def __str__(self):
        return f"{self.name_arabic} في المرتبة {self.rank}"
    
    
