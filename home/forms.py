from django import forms
from .models import contact_us

class contact_Form(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = [
            'date',
            'name',
            'phone_number',
            'gender',
            'ward',
            'location',
            'sub_location',
            'message',
            
        ]
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder':'name'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder':'id_number'}),
            
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder':'0768241496'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'ward': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.Select(attrs={'class': 'form-select'}),
            'sub_location': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder':'message'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }
