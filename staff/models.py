# models.py

from typing import Any
from django.db import models


    

class Corousel_Images(models.Model):
    corousel_images = models.ImageField(upload_to='static/img/corousel',  blank=False,
                            null=False)
    COROUSEL_CHOICES = (
        ('busary', 'busary'),
        ("oppotunity", "oppotunity"),
        ("proffessionals", "proffessionals"),
        ('appointment', 'appointment'),
        ('diaspora', 'diaspora'),
    )
    corousel_type = models.CharField(max_length=50, choices=COROUSEL_CHOICES,
                                 blank=False,
                            null=False)


    
class Outlook_Images(models.Model):
      
    outlook_images = models.ImageField(upload_to='static/img/outlook',  blank=False,
                            null=False)
    
    
    
    
    
class Busary_Images(models.Model):
    busary_images = models.ImageField(upload_to='static/img/busary',  blank=False,
                            null=False)
    
    
class Event_Images(models.Model):
    events_images = models.ImageField(upload_to='static/img/events')
    EVENT_CHOICES = (
        ('Upcoming', 'Upcoming'),
        ('Past', 'Past'),
        
    )
    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES
                            )
    
class Team_Images(models.Model):
    image_title=models.CharField(max_length=20)
    image_name=models.CharField(max_length=20)
    team_images = models.ImageField(upload_to='static/img/team')
    
    
class Upcoming_Project_Images(models.Model):
    Upcoming_Project = models.ImageField(upload_to='static/img/projects/upcoming',  blank=False,
                            null=False)

class Past_Project_Images(models.Model):
    Past_Project = models.ImageField(upload_to='static/img/projects/past',  blank=False,
                            null=False)
    
class Ongoing_Project_Images(models.Model): 
    Ongoing_Project = models.ImageField(upload_to='static/img/projects/ongoing',  blank=False,
                            null=False)
    