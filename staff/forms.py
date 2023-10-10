from django import forms
from .models import *

class Corousel_Images_Form(forms.ModelForm):
    class Meta:
        model=Corousel_Images
        fields = [
            
            'corousel_type',
            'corousel_images',
        ]
        
class Outlook_Images_Form(forms.ModelForm):
    class Meta:
        model=Outlook_Images
        fields = [
            
            
            'outlook_images',
        ]

        

class Busary_Images_Form(forms.ModelForm):
    class Meta:
        model=Busary_Images
        fields=[
            'busary_images'
        ]
         
      
        
class Event_Images_Form(forms.ModelForm):
    class Meta:
        model=Event_Images
        fields=[
            'events_images',
            'event_type',
        ]
        
        widgets = {
            'event_type': forms.Select(attrs={'class': 'form-select','placeholder':'MP, Secretary'}),

        } 
        
       
class Team_Images_Form(forms.ModelForm):
    class Meta:
        model=Team_Images
        fields=[
            'image_title',
            'image_name',
            'team_images',
        ]
        widgets = {
            'image_title': forms.TextInput(attrs={'class': 'form-control','placeholder':'MP, Secretary'}),
            'image_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'HON Karuri'}),

        }
        
class Ongoing_Project_Images_Form(forms.ModelForm):
    class Meta:
        model=Ongoing_Project_Images
        fields=[
            'Ongoing_Project'
        ]
        

class Upcoming_Project_Images_Form(forms.ModelForm):
    class Meta:
        model=Upcoming_Project_Images
        fields=[
            'Upcoming_Project',
        ]
        
class Past_Project_Images_Form(forms.ModelForm):
    class Meta:
        model=Past_Project_Images
        fields=[
            'Past_Project',
        ]