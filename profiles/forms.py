from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'full_name',
            'email',
            'phone_number'
        ]


class AgentProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'company_name',
            'full_name',
            'email',
            'phone_number',
            'address',
            'psr_number',
            'company_logo',
        ]
