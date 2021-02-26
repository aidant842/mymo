from django import forms

from listings.models import SaleListing, RentListing


class DateInputWidget(forms.DateInput):
    input_type = 'date'


class SaleListingForm(forms.ModelForm):
    FACILITY_CHOICES = [
        ('', 'Select Facility'),
        ('Alarm', 'Alarm'),
        ('Gas Fired Central Heating', 'Gas Fired Central Heating'),
        ('Oil Fired Central Heating', 'Oil Fired Central Heating'),
        ('Parking', 'Parking'),
        ('wheelchair Access', 'wheelchair Access'),
        ('Wired for Cable Television', 'Wired for Cable Television'),
    ]

    PROPERTY_TYPE_CHOICES = [
        ('', 'Select type of property'),
        ('Apartment', 'Apartment'),
        ('Bungalow', 'Bungalow'),
        ('Duplex', 'Duplex'),
        ('House', 'House'),
        ('Site', 'Site'),
        ('Studio Apartment', 'Studio Apartment'),
    ]

    SELLING_TYPE_CHOICES = [
        ('', 'Select type of sale'),
        ('Private Treaty', 'Private Treaty'),
        ('Public Auction', 'Public Auction'),
        ('Public Tender', 'Public Tender'),
        ('Private Tender', 'Private Tender'),
    ]

    FLOOR_AREA_TYPE_CHOICES = [
        ('Square Meters', 'Square Meters'),
        ('Feet', 'Feet'),
        ('Acres', 'Acres'),
        ('Hectares', 'Hectares'),
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
    ]

    TAX_DESIGNATION_CHOICES = [
        ('', 'Select Option'),
        ('Not a tax based property', 'Not a tax based property'),
        ('Section 23', 'Section 23'),
        ('Section 27', 'Section 27'),
        ('Section 50', 'Section 50'),
        ('Holiday Home', 'Holiday Home'),
        ('Section 48', 'Section 48'),
    ]

    facility_1 = forms.CharField(widget=forms.Select
                                 (choices=FACILITY_CHOICES), required=False)
    facility_2 = forms.CharField(widget=forms.Select
                                 (choices=FACILITY_CHOICES), required=False)
    facility_3 = forms.CharField(widget=forms.Select
                                 (choices=FACILITY_CHOICES), required=False)
    facility_4 = forms.CharField(widget=forms.Select
                                 (choices=FACILITY_CHOICES), required=False)
    facility_5 = forms.CharField(widget=forms.Select
                                 (choices=FACILITY_CHOICES), required=False)
    facility_6 = forms.CharField(widget=forms.Select
                                 (choices=FACILITY_CHOICES), required=False)
    property_type = forms.CharField(widget=forms.Select
                                    (choices=PROPERTY_TYPE_CHOICES))
    selling_type = forms.CharField(widget=forms.Select
                                   (choices=SELLING_TYPE_CHOICES))
    floor_area_type = forms.CharField(widget=forms.Select
                                      (choices=FLOOR_AREA_TYPE_CHOICES))
    ber_rating = forms.CharField(widget=forms.Select
                                 (choices=BER_CHOICES))
    tax_designation = forms.CharField(widget=forms.Select
                                      (choices=TAX_DESIGNATION_CHOICES))

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
            'images',
        ]

        def __init__(self, *args, **kwargs):
            """ Add placeholders and classes, remove auto generated labels
                and set autofocus on first field """

            super().__init__(*args, **kwargs)

            self.fields['full_name'].widget.attrs['autofocus'] = True
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-style'


class RentListingForm(forms.ModelForm):
    FACILITY_CHOICES = [
        ('', 'Select Facility'),
        ('Alarm', 'Alarm'),
        ('Gas Fired Central Heating', 'Gas Fired Central Heating'),
        ('Oil Fired Central Heating', 'Oil Fired Central Heating'),
        ('Parking', 'Parking'),
        ('wheelchair Access', 'wheelchair Access'),
        ('Wired for Cable Television', 'Wired for Cable Television'),
    ]

    PROPERTY_TYPE_CHOICES = [
        ('', 'Select type of property'),
        ('Apartment', 'Apartment'),
        ('Bungalow', 'Bungalow'),
        ('Duplex', 'Duplex'),
        ('House', 'House'),
        ('Site', 'Site'),
        ('Studio Apartment', 'Studio Apartment'),
    ]

    FLOOR_AREA_TYPE_CHOICES = [
        ('Square Meters', 'Square Meters'),
        ('Feet', 'Feet'),
        ('Acres', 'Acres'),
        ('Hectares', 'Hectares'),
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
    ]

    LEASE_TERM_CHOICES = [
        ('No Minimum Lease', 'No Minimum Lease'),
        ('3 Months', '3 Months'),
        ('6 Months', '6 Months'),
        ('9 Months', '9 Months'),
        ('1 Year', '1 Year'),
        ('2 Years', '2 Years'),
        ('3 Years', '3 Years'),
    ]

    FURNISHING_CHOICES = [
        ('', 'Select furnished type'),
        ('Furnished', 'Furnished'),
        ('Unfurnished', 'Unfurnished'),
        ('Either', 'Either'),
    ]

    RENT_TYPE_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Weekly', 'Weekly'),
    ]

    facility_1 = forms.CharField(widget=forms.Select
                                 (choices=FACILITY_CHOICES), required=False)
    facility_2 = forms.CharField(widget=forms.Select
                                 (choices=FACILITY_CHOICES), required=False)
    facility_3 = forms.CharField(widget=forms.Select
                                 (choices=FACILITY_CHOICES), required=False)
    facility_4 = forms.CharField(widget=forms.Select
                                 (choices=FACILITY_CHOICES), required=False)
    facility_5 = forms.CharField(widget=forms.Select
                                 (choices=FACILITY_CHOICES), required=False)
    facility_6 = forms.CharField(widget=forms.Select
                                 (choices=FACILITY_CHOICES), required=False)
    property_type = forms.CharField(widget=forms.Select
                                    (choices=PROPERTY_TYPE_CHOICES))
    floor_area_type = forms.CharField(widget=forms.Select
                                      (choices=FLOOR_AREA_TYPE_CHOICES))
    ber_rating = forms.CharField(widget=forms.Select
                                 (choices=BER_CHOICES))
    lease_term = forms.CharField(widget=forms.Select
                                 (choices=LEASE_TERM_CHOICES))
    furnishing = forms.CharField(widget=forms.Select
                                 (choices=FURNISHING_CHOICES))
    rent_type = forms.CharField(widget=forms.Select
                                (choices=RENT_TYPE_CHOICES))

    class Meta:
        model = RentListing
        widgets = {'available_from': DateInputWidget()}
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
            'floor_area_type',
            'floor_area',
            'ber_rating',
            'description',
            'images',
        ]

        def __init__(self, *args, **kwargs):
            """ Add placeholders and classes, remove auto generated labels
                and set autofocus on first field """

            super().__init__(*args, **kwargs)

            self.fields['full_name'].widget.attrs['autofocus'] = True
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-style'
