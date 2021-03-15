from django import forms

from localflavor.ie.ie_counties import IE_COUNTY_CHOICES


class FilterForm(forms.Form):

    PROPERTY_TYPE_CHOICES = [
        ('', 'Select type of property'),
        ('Apartment', 'Apartment'),
        ('Bungalow', 'Bungalow'),
        ('Duplex', 'Duplex'),
        ('House', 'House'),
        ('Site', 'Site'),
        ('Studio Apartment', 'Studio Apartment'),
    ]

    BER_CHOICES = [
        ('', 'Select Option'),
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
        ('', 'Select Category'),
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    ]

    price = forms.IntegerField(widget=forms.NumberInput(
                               attrs={'placeholder': 'Max (€)'}),
                               label='')

    bedrooms = forms.IntegerField(widget=forms.NumberInput(
                                   attrs={'placeholder': 'Bedrooms'}),
                                  label='')

    bathrooms = forms.IntegerField(widget=forms.NumberInput(
                                    attrs={'placeholder': 'Bathrooms'}),
                                   label='')

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
