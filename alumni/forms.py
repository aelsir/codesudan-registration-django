from django import forms
from .models import Alumni

class AlumniRegistrationForm(forms.ModelForm):
    class Meta:
        model = Alumni
        exclude = ('alumni',)
        labels = {
            'language': 'لغة البرمجة',
            'framework': 'إطار العمل',
            'facebook_url': 'رابط حسابك على فيسبوك',
            'linkedin_url': 'رابط حسابك على لينكدان',
            'twitter_url': 'رابط حسابك على تويتر',
            'whatsapp_number': 'رقم الواتساب'
            }
        required = (
            'language',
            'framework',
        )
        widgets = {
            "language": forms.Select(attrs={"class": "form-select"}),
            'framework': forms.Select(attrs={"class": "form-select"}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control'}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control'}),
        }