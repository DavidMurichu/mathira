from django import forms
from .models import *

class Corousel_Images_Form(forms.ModelForm):
    class Meta:
        model=Corousel_Images
        fields = [
            
            'corousel_type',
            'Corousel',
        ]
        
class Outlook_Images_Form(forms.ModelForm):
    class Meta:
        model=Outlook_Images
        fields = [
            
            
            'Outlook',
        ]

        

class Busary_Images_Form(forms.ModelForm):
    class Meta:
        model=Busary_Images
        fields=[
            'Busary'
        ]
         
      
        
class Event_Images_Form(forms.ModelForm):
    class Meta:
        model=Event_Images
        fields=[
            'Event',
            'event_type',
            'event_name',
            'event_agenda',
            'event_place',
            'event_date',
        ]
        
        widgets = {
            'event_place': forms.TextInput(attrs={'class': 'form-control','placeholder':'event place'}),
            'event_agenda': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'event agenda'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'event name'}),
            'event_type': forms.Select(attrs={'class': 'form-select','placeholder':'MP, Secretary'}),
        } 
        
       
class Team_Images_Form(forms.ModelForm):
    class Meta:
        model=Team_Images
        fields=[
            'image_title',
            'image_name',
            'Team',
        ]
        widgets = {
            'image_title': forms.TextInput(attrs={'class': 'form-control','placeholder':'MP, Secretary'}),
            'image_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'HON Karuri'}),

        }
        
class Project_Images_Form(forms.ModelForm):
    class Meta:
        model=Project_Images
        fields=[
            'Project',
            'project_name',
            'project_location',
            'project_date',
            'project_type'
        ]
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'project_name'}),
            'project_date': forms.DateInput(attrs={'class': 'form-control'}),
            'project_location': forms.TextInput(attrs={'class': 'form-control','placeholder':'project_location'}),
            'project_type':forms.Select(attrs={'class':'form-select'})
        }