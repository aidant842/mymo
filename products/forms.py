from django import forms

from listings.models import SaleListing, RentListing


class SaleListingForm(forms.ModelForm):
    class Meta:
        model = SaleListing
        fields = [
            'category',
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
    class Meta:
        model = RentListing
        fields = [
            'category',
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
            'facility_1',
            'facility_2',
            'facility_3',
            'facility_4',
            'facility_5',
            'facility_6',
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
