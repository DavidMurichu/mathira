from django import forms
from .models import Proffession

class Prof_Form(forms.ModelForm):
    class Meta:
        model = Proffession
        fields = [
            'date',
            
            'name',
            
            'email',
            
            'id_number',
            
            'phone_number',
            
            'gender',
            
            'education_level',
            
            'proffession',
            
            'ward',
            
            'age',
            
            'location',
            
            'sub_location',
            
            
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder':'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                           'placeholder':'optional(hello@gmail.com)'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder':'id_number'}),
            
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder':'0768241496'}),
            'age': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder':'age'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'education_level': forms.Select(attrs={'class': 'form-select'}),
            'proffession': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder':'Proffession'}),
            'ward': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.Select(attrs={'class': 'form-select'}),
            'sub_location': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }