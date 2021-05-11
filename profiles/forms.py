from django import forms
from .models import UserProfile

from allauth.account.forms import LoginForm, SignupForm


class SelfLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["login"].label = ""
        self.fields["password"].label = ""


class SelfSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].label = ""
        self.fields["email2"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""
        self.fields["email"].widget.attrs['placeholder'] = "Email"
        self.fields["email2"].widget.attrs['placeholder'] = "Confirm Email"
        self.fields["password1"].widget.attrs['placeholder'] = "Password"
        self.fields["password2"].widget.attrs['placeholder'] = "Confirm Password"


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'full_name',
            'email',
            'phone_number'
        ]


class AgentProfileForm(forms.ModelForm):
    company_logo = forms.FileField(widget=forms.ClearableFileInput(
                                    attrs={
                                        'class': 'form-control',
                                    }),
                                   required=False)

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
