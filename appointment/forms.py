from django import forms
from .models import appointment

class app_Form(forms.ModelForm):
    class Meta:
        model = appointment
        fields = [
            'date',
            'name',
            'id_number',
            'phone_number',
            'gender',
            'education_level',
            'agenda',
            'ward',
            'age',
            'location',
            'sub_location',
            
            
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder':'name'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder':'id_number'}),
            
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder':'0768241496'}),
            'age': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder':'age'}),
            'gender': forms.Select(attrs={'class': 'form-select','placeholder':'agenda'}),
            'education_level': forms.Select(attrs={'class': 'form-select'}),
            'agenda': forms.Textarea(attrs={'class': 'form-control',
                                            'placeholder': 'Write A Summary of your Agender '}),
            'ward': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.Select(attrs={'class': 'form-select'}),
            'sub_location': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }
