from django import forms


class AgentFilter(forms.Form):
    IE_COUNTY_CHOICES = [
        (None, 'County'), ('carlow', 'Carlow'), ('cavan', 'Cavan'),
        ('clare', 'Clare'), ('cork', 'Cork'),
        ('donegal', 'Donegal'), ('dublin', 'Dublin'),
        ('galway', 'Galway'), ('kerry', 'Kerry'),
        ('kildare', 'Kildare'), ('kilkenny', 'Kilkenny'),
        ('laois', 'Laois'), ('leitrim', 'Leitrim'),
        ('limerick', 'Limerick'), ('longford', 'Longford'),
        ('louth', 'Louth'), ('mayo', 'Mayo'),
        ('meath', 'Meath'), ('monaghan', 'Monaghan'),
        ('offaly', 'Offaly'), ('roscommon', 'Roscommon'),
        ('sligo', 'Sligo'), ('tipperary', 'Tipperary'),
        ('waterford', 'Waterford'), ('westmeath', 'Westmeath'),
        ('wexford', 'Wexford'), ('wicklow', 'Wicklow'),
    ]

    county = forms.CharField(widget=forms.Select
                             (choices=IE_COUNTY_CHOICES,
                              attrs={'class': 'form-select'}),
                             label='',
                             required=False)
    name = forms.CharField(widget=forms.TextInput(
                            attrs={'placeholder': 'Name'}),
                           label="",
                           required=False)


class ContactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(
                            attrs={'placeholder': 'Full Name (required)'}),
                           label="",
                           required=True)
    email = forms.EmailField(widget=forms.TextInput(
                             attrs={'type': 'email',
                                    'placeholder': 'E-mail address (required)'}),
                             label="",
                             required=True)

    phone_number = forms.CharField(widget=forms.TextInput(
                            attrs={'placeholder': 'Phone'}),
                           label="",
                           required=False)

    message = forms.CharField(widget=forms.Textarea(
                              attrs={'placeholder': 'Your Message (required)'}),
                              label="",
                              required=True)
