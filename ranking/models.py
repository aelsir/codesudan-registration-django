from django.db import models

# Create your models here.

class Developer(models.Model):

    class Countries(models.TextChoices):
        SUDAN = 'sd', 'السودان'
    name_arabic = models.CharField(max_length=64)
    name_english = models.CharField(max_length=64)
    country = models.CharField(max_length=2, choices=Countries.choices, default=Countries.SUDAN)
    contribs = models.IntegerField(blank=True, null=True)
    facebook_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)

    class Meta:
        permissions = [
            ('contributor', "add or remove in developer ranking")
        ]

    def __str__(self):
        return f"{self.name_arabic} إسهامات  {self.contribs}"
    
    
