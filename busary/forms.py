from django import forms
from .models import Busary

class Bus_Form(forms.ModelForm):
    class Meta:
        model=Busary
        fields = [
            'date',
            'name',
            'admission_number',
            'school_name',
            'parent_name',
            'education_level',
            'phone_number',         
            'gender',
            'amount',
            'ward',    
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder':'name'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control',
                                                   'placeholder':'Amount(KSH)'}),
            
            'school_name': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder':'school_name'}),
            'parent_name': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder':'parent_name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder':'phone_number'}),
            'education_level': forms.Select(attrs={'class': 'form-select'}),
            
            'admission_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder':'admission_number'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            
            'ward': forms.Select(attrs={'class': 'form-select'}),
           
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }

