from django import forms
from .models import project

class proj_Form(forms.ModelForm):
    class Meta:
        model = project
        fields = [
            'date',
            'name',
            'phone_number',
            'project_description',
            'ward',
            'location',
            'sub_location',
            'project',
            
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder':'name'}),
            'project_description': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder':'Repair of Kartina Kagochi Road'}),
            'project': forms.Select(attrs={'class': 'form-select'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder':'0768241466'}),

            'ward': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.Select(attrs={'class': 'form-select'}),
            'sub_location': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }
