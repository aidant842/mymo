from django import forms
from ckeditor.widgets import CKEditorWidget

from listings.models import (SaleListing, RentListing,
                             SaleListingImage, RentListingImage)


class DateInputWidget(forms.DateInput):
    input_type = 'date'


class SaleListingForm(forms.ModelForm):

    PROPERTY_TYPE_CHOICES = [
        ('', 'Select type of property *'),
        ('House', 'House'),
        ('Terraced House', 'Terraced House'),
        ('Detached house', 'Detached house'),
        ('Semi-detached house', 'Semi-detached house'),
        ('Townhouse', 'Townhouse'),
        ('Repossessed House', 'Repossessed House'),
        ('Bungalow', 'Bungalow'),
        ('Cottage', 'Cottage'),
        ('Manor', 'Manor'),
        ('Apartment', 'Apartment'),
        ('Studio Apartment', 'Studio Apartment'),
        ('Duplex', 'Duplex'),
        ('Site', 'Site'),
        ('Land', 'Land'),
        ('Commercial Unit', 'Commercial Unit'),
        ('Industrial Unit', 'Industrial Unit'),
    ]

    SELLING_TYPE_CHOICES = [
        ('', 'Select type of sale *'),
        ('Private Treaty', 'Private Treaty'),
        ('Public Auction', 'Public Auction'),
        ('Public Tender', 'Public Tender'),
        ('Private Tender', 'Private Tender'),
    ]

    FLOOR_AREA_TYPE_CHOICES = [
        ('Square Meters', 'Square Meters'),
        ('Square Feet', 'Square Feet'),
        ('Acres', 'Acres'),
        ('Hectares', 'Hectares'),
    ]

    BER_CHOICES = [
        ('', 'BER Rating *'),
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
        ('exempt', 'BER exempt'),
    ]

    TAX_DESIGNATION_CHOICES = [
        ('', 'Tax Designation *'),
        ('Not a tax based property', 'Not a tax based property'),
        ('Section 23', 'Section 23'),
        ('Section 27', 'Section 27'),
        ('Section 50', 'Section 50'),
        ('Holiday Home', 'Holiday Home'),
        ('Section 48', 'Section 48'),
    ]

    IE_COUNTY_CHOICES = [
        (None, 'County *'), ('carlow', 'Carlow'), ('cavan', 'Cavan'),
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

    property_type = forms.CharField(widget=forms.Select
                                    (choices=PROPERTY_TYPE_CHOICES,
                                     attrs={'class': 'form-select form-control'}))
    selling_type = forms.CharField(widget=forms.Select
                                   (choices=SELLING_TYPE_CHOICES,
                                    attrs={'class': 'form-select form-control'}))
    floor_area_type = forms.CharField(widget=forms.Select
                                      (choices=FLOOR_AREA_TYPE_CHOICES,
                                       attrs={'class': 'form-select form-control'}))
    ber_rating = forms.CharField(widget=forms.Select
                                 (choices=BER_CHOICES,
                                  attrs={'class': 'form-select form-control'}))
    tax_designation = forms.CharField(widget=forms.Select
                                      (choices=TAX_DESIGNATION_CHOICES,
                                       attrs={'class': 'form-select form-control'}))
    header_image = forms.FileField(widget=forms.ClearableFileInput(
                                   attrs={
                                       'name': 'images',
                                       'onchange': 'readHeaderURL(this);',
                                       'accept': 'image/*',
                                       'class': 'form-control',
                                    }),
                                   required=True)
    county = forms.CharField(widget=forms.Select
                             (choices=IE_COUNTY_CHOICES,
                              attrs={'class': 'form-select form-control'}))
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = SaleListing
        fields = [
            'company_name',
            'full_name',
            'email',
            'phone',
            'call_between_hrs',
            'county',
            'area',
            'eircode',
            'property_type',
            'selling_type',
            'price',
            'poa',
            'no_of_bedrooms',
            'no_of_bathrooms',
            'facility_1',
            'facility_2',
            'facility_3',
            'facility_4',
            'facility_5',
            'facility_6',
            'floor_area_type',
            'floor_area',
            'ber_rating',
            'tax_designation',
            'top_features_1',
            'top_features_2',
            'top_features_3',
            'top_features_4',
            'top_features_5',
            'description',
            'header_image',
        ]

    def __init__(self, *args, **kwargs):

        """ Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field """

        super().__init__(*args, **kwargs)
        placeholders = {
            'company_name': 'Company Name',
            'full_name': 'Full Name',
            'email': 'E-mail Address',
            'phone': 'Phone Number',
            'call_between_hrs': 'Available Hours',
            'county': 'County',
            'area': 'Town/Area',
            'eircode': 'Eircode',
            'property_type': 'Property Type',
            'selling_type': 'Type of Sale',
            'price': '€ Property Price',
            'poa': 'POA',
            'no_of_bedrooms': 'Number of bedrooms',
            'no_of_bathrooms': 'Number of bathrooms',
            'facility_1': 'First Facility',
            'facility_2': 'Second Facility',
            'facility_3': 'Third Facility',
            'facility_4': 'Fourth Facility',
            'facility_5': 'Fifth Facility',
            'facility_6': 'Sixth Facility',
            'floor_area_type': 'Floor Area Type',
            'floor_area': 'Floor Area',
            'ber_rating': 'BER Rating',
            'tax_designation': 'Tax Designation',
            'top_features_1': 'First Top Feature',
            'top_features_2': 'Second Top Feature',
            'top_features_3': 'Third Top Feature',
            'top_features_4': 'Fourth Top Feature',
            'top_features_5': 'Fifth Top Feature',
            'description': 'Description',
            'header_image': 'Header Image',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['placeholder'] = placeholder
            """ self.fields[field].widget.attrs['validate'] = True """
            if field != 'poa' and field != 'header_image':
                self.fields[field].label = False


class RentListingForm(forms.ModelForm):

    PROPERTY_TYPE_CHOICES = [
        ('', 'Select type of property *'),
        ('House', 'House'),
        ('Terraced House', 'Terraced House'),
        ('Detached house', 'Detached house'),
        ('Semi-detached house', 'Semi-detached house'),
        ('Townhouse', 'Townhouse'),
        ('Repossessed House', 'Repossessed House'),
        ('Bungalow', 'Bungalow'),
        ('Cottage', 'Cottage'),
        ('Manor', 'Manor'),
        ('Apartment', 'Apartment'),
        ('Studio Apartment', 'Studio Apartment'),
        ('Duplex', 'Duplex'),
        ('Site', 'Site'),
        ('Land', 'Land'),
        ('Commercial Unit', 'Commercial Unit'),
        ('Industrial Unit', 'Industrial Unit'),
    ]

    FLOOR_AREA_TYPE_CHOICES = [
        ('Square Meters', 'Square Meters'),
        ('Square Feet', 'Square Feet'),
        ('Acres', 'Acres'),
        ('Hectares', 'Hectares'),
    ]

    BER_CHOICES = [
        ('', 'BER Rating *'),
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
        ('exempt', 'BER exempt'),
    ]

    LEASE_TERM_CHOICES = [
        ('', 'Lease Term *'),
        ('No Minimum Lease', 'No Minimum Lease'),
        ('3 Months', '3 Months'),
        ('6 Months', '6 Months'),
        ('9 Months', '9 Months'),
        ('1 Year', '1 Year'),
        ('2 Years', '2 Years'),
        ('3 Years', '3 Years'),
    ]

    FURNISHING_CHOICES = [
        ('', 'Select furnished type *'),
        ('Furnished', 'Furnished'),
        ('Unfurnished', 'Unfurnished'),
        ('Either', 'Either'),
    ]

    RENT_TYPE_CHOICES = [
        ('', 'Rent Type *'),
        ('Night', 'Per Night'),
        ('Week', 'Per Week'),
        ('Month', 'Per Month'),
        ('Year', 'Per Year'),
    ]

    IE_COUNTY_CHOICES = [
        (None, 'County *'), ('carlow', 'Carlow'), ('cavan', 'Cavan'),
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

    property_type = forms.CharField(widget=forms.Select
                                    (choices=PROPERTY_TYPE_CHOICES,
                                     attrs={'class': 'form-select'}))
    floor_area_type = forms.CharField(widget=forms.Select
                                      (choices=FLOOR_AREA_TYPE_CHOICES,
                                       attrs={'class': 'form-select'}))
    ber_rating = forms.CharField(widget=forms.Select
                                 (choices=BER_CHOICES,
                                  attrs={'class': 'form-select'}))
    lease_term = forms.CharField(widget=forms.Select
                                 (choices=LEASE_TERM_CHOICES,
                                  attrs={'class': 'form-select'}))
    furnishing = forms.CharField(widget=forms.Select
                                 (choices=FURNISHING_CHOICES,
                                  attrs={'class': 'form-select'}))
    rent_type = forms.CharField(widget=forms.Select
                                (choices=RENT_TYPE_CHOICES,
                                 attrs={'class': 'form-select'}))
    header_image = forms.FileField(widget=forms.ClearableFileInput(
                                   attrs={
                                       'name': 'images',
                                       'onchange': 'readHeaderURL(this);',
                                       'accept': 'image/*',
                                       'class': 'form-control',
                                    }),
                                   required=True)
    county = forms.CharField(widget=forms.Select
                             (choices=IE_COUNTY_CHOICES,
                              attrs={'class': 'form-select'}))

    available_from = forms.CharField(widget=forms.TextInput(
        attrs={'onfocus': '(this.type="date")', 'onblur': '(this.type="text")',
               'localize': 'true'}
    ))
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = RentListing
        """ widgets = {'available_from': DateInputWidget()} """
        fields = [
            'company_name',
            'full_name',
            'email',
            'phone',
            'call_between_hrs',
            'county',
            'area',
            'eircode',
            'property_type',
            'rent_type',
            'price',
            'poa',
            'available_from',
            'lease_term',
            'no_of_single_bedrooms',
            'no_of_double_bedrooms',
            'no_of_twin_bedrooms',
            'no_of_bathrooms',
            'furnishing',
            'facility_1',
            'facility_2',
            'facility_3',
            'facility_4',
            'facility_5',
            'facility_6',
            'top_features_1',
            'top_features_2',
            'top_features_3',
            'top_features_4',
            'top_features_5',
            'floor_area_type',
            'floor_area',
            'ber_rating',
            'description',
            'header_image',
        ]

    def __init__(self, *args, **kwargs):

        """ Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field """

        super().__init__(*args, **kwargs)
        placeholders = {
            'company_name': 'Company Name',
            'full_name': 'Full Name',
            'email': 'E-mail Address',
            'phone': 'Phone Number',
            'call_between_hrs': 'Available Hours',
            'county': 'County',
            'area': 'Town/Area',
            'eircode': 'Eircode',
            'property_type': 'Property Type',
            'rent_type': 'Type of Rent',
            'price': '€ Property Price',
            'poa': 'POA',
            'available_from': 'Available From',
            'lease_term': 'Lease Term',
            'no_of_single_bedrooms': 'No. Single Bedrooms',
            'no_of_double_bedrooms': 'No. Double Bedrooms',
            'no_of_twin_bedrooms': 'No. Twin Bedrooms',
            'no_of_bathrooms': 'No. bathrooms',
            'furnishing': 'Furnishing',
            'facility_1': 'First Facility',
            'facility_2': 'Second Facility',
            'facility_3': 'Third Facility',
            'facility_4': 'Fourth Facility',
            'facility_5': 'Fifth Facility',
            'facility_6': 'Sixth Facility',
            'floor_area_type': 'Floor Area Type',
            'floor_area': 'Floor Area',
            'ber_rating': 'BER Rating',
            'tax_designation': 'Tax Designation',
            'top_features_1': 'First Top Feature',
            'top_features_2': 'Second Top Feature',
            'top_features_3': 'Third Top Feature',
            'top_features_4': 'Fourth Top Feature',
            'top_features_5': 'Fifth Top Feature',
            'description': 'Description',
            'header_image': 'Header Image',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['placeholder'] = placeholder
            if field != 'poa' and field != 'header_image':
                self.fields[field].label = False


class SaleImageForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(
                             attrs={
                                 'name': 'images',
                                 'onchange': 'readURL(this);',
                                 'multiple': True,
                                 'accept': 'image/*',
                                 'class': 'form-control',
                             }),
                             required=True,)

    class Meta:
        model = SaleListingImage
        fields = [
            'images'
        ]


class RentImageForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(
                             attrs={
                                 'name': 'images',
                                 'onchange': 'readURL(this);',
                                 'multiple': True,
                                 'accept': 'image/*',
                                 'class': 'form-control',
                             }),
                             required=True)

    class Meta:
        model = RentListingImage
        fields = [
            'images'
        ]
