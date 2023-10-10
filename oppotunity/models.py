from django.db import models
import pycountry
from django.utils.timezone import now
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator

class Common_oppotunities(models.Model):
    date = models.DateField(default=now)
    name = models.CharField(max_length=50,
                            blank=False,
                            null=False)
    id_number = models.CharField(max_length=8,
       
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
    
    EDUCATION_CHOICES = (
        ('High School', 'High School'),
        ("Bachelor's Degree", "Bachelor's Degree"),
        ("Master's Degree", "Master's Degree"),
        ('Ph.D.', 'Ph.D.'),
        ('Other', 'Other'),
    )
    education_level = models.CharField(max_length=50, choices=EDUCATION_CHOICES,
                                 blank=False,
                            null=False)
    
    EMPLOYMENT_CHOICES = (
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed'),
        ('Student', 'Student'),
        ('Other', 'Other'),
    )
    employment_status = models.CharField(max_length=50, choices=EMPLOYMENT_CHOICES,
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

    LOCATION_CHOICES = (
         ('Magutu', 'Magutu'),
    ('Konyu', 'Konyu'),
    ('Mugunda', 'Mugunda'),
    ('Ruguru', 'Ruguru'),
    ('Karatina', 'Karatina'),
    ('Kiawara', 'Kiawara'),
    ('Gatitu', 'Gatitu'),
    ('Gitugi', 'Gitugi'),
    ('Iriaini', 'Iriaini'),
    ('Muhito', 'Muhito'),
    ('Karima', 'Karima'),
    ('Rwathia', 'Rwathia'),
    ('Thunguma', 'Thunguma'),
    ('Muruguru', 'Muruguru'),
    ('Kagochi', 'Kagochi'),
    ('Kiriita', 'Kiriita'),
    ('Kiamathura', 'Kiamathura'),
    ('Gakawa', 'Gakawa'),
    ('Kiangoma', 'Kiangoma'),
    ('Ngangarithi', 'Ngangarithi'),
    ('Gakindu', 'Gakindu'),
    )
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES,
                                 blank=False,
                            null=False)
    SUB_LOCATION_CHOICES = (
        ('SubLocation1', 'Sub-Location 1'),
        ('SubLocation2', 'Sub-Location 2'),
        ('SubLocation3', 'Sub-Location 3'),
        ('Other', 'Other'),
    )
    sub_location = models.CharField(max_length=50, choices=SUB_LOCATION_CHOICES,
                                 blank=False,
                            null=False)
    COUNTRY_CHOICES = [(country.alpha_2, country.name) for country in pycountry.countries]
    country_Code=models.CharField(max_length=50, choices=COUNTRY_CHOICES, default='KE',
                                 blank=False,
                            null=False)
    class Meta:
        abstract=True

class oppotunities(Common_oppotunities):
    def __str__(self):
        return 'oppotunities'


class oppotunitiesapproved(Common_oppotunities):
    def __str__(self):
        return 'oppotunitiesapproved'
    