from django.db import models
from django.utils.timezone import now


# Create your models here.
class Common_Busary(models.Model):
    date = models.DateField(default=now)
    name = models.CharField(max_length=50,
                            blank=False,
                            null=False)

    admission_number = models.CharField(max_length=50,
                            blank=False,
                            null=False)
    school_name = models.CharField(max_length=50,
                            blank=False,
                            null=False)
    parent_name = models.CharField(max_length=50,
                            blank=False,
                            null=False)
    
    EDUCATION_CHOICES = (
        ('High School', 'High School'),
        ("Collage", "Collage"),
        ("University", "University"),
    )
    education_level = models.CharField(max_length=50, choices=EDUCATION_CHOICES,
                                 blank=False,
                            null=False)
    
    amount = models.IntegerField(
                            blank=False,
                            null=False)
    
 
    phone_number = models.CharField(
        max_length=10,
                                 blank=False,
                            null=False
    ) 
    
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
                                 blank=False,
                            null=False)
    
   
    


    WARD_CHOICES = (
    ('Magutu', 'Magutu'),
    ('Konyu', 'Konyu'),
    ('Iria-ini', 'Iria-ini'),
    ('Ruguru', 'Ruguru'),
    ('Giathieko', 'Giathieko'),
    ('Gikondi', 'Gikondi'),
    ('Karatina Town', 'Karatina Town'),
    ('Kiamathaga', 'Kiamathaga'),
    )
    ward = models.CharField(max_length=50, choices=WARD_CHOICES,
                                 blank=False,
                            null=False)

   
    class Meta:
        abstract=True
    
    
class Busary(Common_Busary):
    pass
class Busaryapproved(Common_Busary):
    pass
  
