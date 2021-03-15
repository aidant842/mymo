from django import forms


class FilterForm(forms.Form):

    PROPERTY_TYPE_CHOICES = [
        (None, 'Select type of property'),
        ('Apartment', 'Apartment'),
        ('Bungalow', 'Bungalow'),
        ('Duplex', 'Duplex'),
        ('House', 'House'),
        ('Site', 'Site'),
        ('Studio Apartment', 'Studio Apartment'),
    ]

    BER_CHOICES = [
        (None, 'BER'),
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A3', 'A3'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('B3', 'B3'),
        ('C1', 'C1'),
        ('C2', 'C2'),
        ('C3', 'C3'),
        ('D1', 'D1'),
        ('D2', 'D2'),
        ('E1', 'E1'),
        ('E2', 'E2'),
        ('F', 'F'),
        ('G', 'G'),
        ('BER exempt', 'BER exempt'),
    ]

    CATEGORY_CHOICES = [
        (None, 'Select Category'),
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    ]

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

    price = forms.IntegerField(widget=forms.NumberInput(
                               attrs={'placeholder': 'Max (€)'}),
                               label='',
                               required=False)

    bedrooms = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Bedrooms'}),
        label='',
        required=False)

    bathrooms = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Bathrooms'}),
        label='',
        required=False)

    property_type = forms.CharField(widget=forms.Select
                                    (choices=PROPERTY_TYPE_CHOICES,
                                     attrs={'class': 'form-select'}),
                                    label='',
                                    required=False)

    ber_rating = forms.CharField(widget=forms.Select
                                 (choices=BER_CHOICES,
                                     attrs={'class': 'form-select'}),
                                 label='',
                                 required=False)

    county = forms.CharField(widget=forms.Select
                             (choices=IE_COUNTY_CHOICES,
                              attrs={'class': 'form-select'}),
                             label='',
                             required=False)

    category = forms.CharField(widget=forms.Select
                               (choices=CATEGORY_CHOICES,
                                attrs={'class': 'form-select'}),
                               label='',
                               required=False)
