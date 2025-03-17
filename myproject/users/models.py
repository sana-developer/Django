from django.contrib.auth.models import AbstractUser
from django.db import models

# Create custom user model
class User(AbstractUser):   # Extending Django's User model
    name = models.CharField(max_length==100, blank=True, null=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField(blank=True, null=True)

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('candidate','Candidate'),
        ('employer','Employer')
    )

# Create your SIMPLE model here.
class User(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    def __str__(self):  
        return self.name
    
    # This creates a users_user table in the database!

