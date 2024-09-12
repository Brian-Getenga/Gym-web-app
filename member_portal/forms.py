from django import forms
from .models import MemberProfile

class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = ['bio', 'birth_date', 'phone_number']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us something about yourself...',
                'rows': 4,
                'style': 'resize:none;',
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD',
                'type': 'date',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
            }),
        }
        labels = {
            'bio': 'Personal Bio',
            'birth_date': 'Date of Birth',
            'phone_number': 'Contact Number',
        }
        help_texts = {
            'bio': 'A brief introduction about yourself.',
            'birth_date': 'Your date of birth in YYYY-MM-DD format.',
            'phone_number': 'Include country code if applicable.',
        }
