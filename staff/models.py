# models.py

from typing import Any
from django.db import models

from django.utils.timezone import now
    

class Corousel_Images(models.Model):
    Corousel = models.ImageField(upload_to='static/img/corousel',  blank=False,
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
      
    Outlook = models.ImageField(upload_to='static/img/outlook',  blank=False,
                            null=False)
    
    
    
    
    
class Busary_Images(models.Model):
    Busary = models.ImageField(upload_to='static/img/busary',  blank=False,
                            null=False)
    
    
class Event_Images(models.Model):
    Event = models.ImageField(upload_to='static/img/events')
    EVENT_CHOICES = (
        ('Upcoming', 'Upcoming'),
        ('Past', 'Past'),
        
    )
    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES                         )
    event_name=models.CharField(max_length=20)
    event_place=models.CharField(max_length=50)
    event_agenda=models.CharField(max_length=50)
    event_date=models.DateField(default=now)
    
class Team_Images(models.Model):
    image_title=models.CharField(max_length=20)
    image_name=models.CharField(max_length=20)
    Team = models.ImageField(upload_to='static/img/team')
    

class Project_Images(models.Model): 
    project_name=models.CharField(max_length=20)
    project_type=models.CharField(max_length=20)
    project_location=models.CharField(max_length=20)
    project_date=models.DateField(default=now)
    Project = models.ImageField(upload_to='static/img/projects',  blank=False,
                            null=False)
    PROJECT_CHOICES = (
        ('Ongoing_Project', 'Ongoing_Project'),
        ("Past_Project", "Past_Project"),
        ("Upcoming_Project", "Upcoming_Project"),
    )
    project_type = models.CharField(max_length=50, choices=PROJECT_CHOICES,
                                 blank=False,
                            null=False)

    