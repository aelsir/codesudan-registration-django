from django import forms
from .models import Alumni

class AlumniRegistrationForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['language', 'framework', 'facebook_url', 'linkedin_url', 'twitter_url', 'whatsapp_number']
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
            'whatsapp_number'
        )
        widgets = {
            
        }