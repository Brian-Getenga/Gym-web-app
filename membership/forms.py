from django import forms
from .models import Membership

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['membership_type', 'start_date', 'end_date']
        widgets = {
            'membership_type': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
        }
