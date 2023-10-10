from django import forms
from .models import oppotunities

class opp_Form(forms.ModelForm):
    class Meta:
        model = oppotunities
        fields = [
            'date',
            'name',
            'id_number',
            'phone_number',
            'gender',
            'education_level',
            'employment_status',
            'ward',
            'location',
            'sub_location',
            'country_Code',
            
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder':'name'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder':'id_number'}),
            'country_Code': forms.Select(attrs={'class': 'form-select'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder':'0768241496'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'education_level': forms.Select(attrs={'class': 'form-select'}),
            'employment_status': forms.Select(attrs={'class': 'form-select'}),
            'ward': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.Select(attrs={'class': 'form-select'}),
            'sub_location': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }
