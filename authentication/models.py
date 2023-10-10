from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_code = models.CharField(max_length=10)

    # Add other profile fields as needed

    def __str__(self):
        return self.user.username
