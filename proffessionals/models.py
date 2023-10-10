from django.db import models



from django.utils.timezone import now
# Create your models here.
class Common_Proffession(models.Model):
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
    
    age = models.CharField(max_length=2,
                                 blank=False,
                            null=False,
                            )
    
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
                                 blank=False,
                            null=False)
    
    
    email= models.EmailField( blank=True,
                             null=True)
    
    


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
    
    

    proffession = models.CharField(max_length=50,
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


    
    class Meta:
        abstract=True



 
class Proffession(Common_Proffession):
    def __str__(self):
        return 'Proffession'

 
class Proffessionapproved(Common_Proffession):
    def __str__(self):
        return 'Proffessionapproved'
    