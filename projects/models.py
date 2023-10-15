from django.db import models
from django.utils.timezone import now
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
class Common_project(models.Model):
    id = models.AutoField(primary_key=True) 
    date = models.DateField(default=now)
    name = models.CharField(max_length=50,
                            blank=False,
                            null=False)
    project_description = models.CharField(max_length=50,
                            blank=False,
                            null=False)

    phone_number = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(limit_value=10, message='Phone number must be at least 10 digits.'),
            MaxLengthValidator(limit_value=10, message='Phone number can have at most 10 digits.'),
            RegexValidator(regex=r'^[0-9]{10}$', message='Phone number must contain only digits.')
        ],
                                 blank=False,
                            null=False
    )              
    

                   
    project_CHOICES = (
        ('NG-CDF Projects', 'NG-CDF Projects'),
        ("Road Projects", "Road Projects"),
        ("Uwezo Fund Program", "Uwezo Fund Program"),
        ('TCDL Programs', 'TCDL Programs'),
        ('Diversity and Inclusion', 'Diversity and Inclusion'),

        ('Other', 'Other'),
    )
    project = models.CharField(max_length=50, choices=project_CHOICES,
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
    class Meta:
        abstract=True
    def __str__(self):
        return 'Common_project'
        


class project(Common_project):
    def __str__(self):
        return 'project'

class projectapproved(Common_project):
    def __str__(self):
        return 'projectapproved'