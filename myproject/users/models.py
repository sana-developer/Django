from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model
class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("candidate", "Candidate"),
        ("employer", "Employer"),
    ]

    # Fields
    name = models.CharField(max_length=100, default="default name")
    email = models.EmailField(unique=True)  # Email as a unique field
    age = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default=None, blank=True, null=True)

    # Remove the username field from the form but keep it in the database
    username = None  # Disable the username field

    # Use email as the unique identifier
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "age", "role"]  # Fields required when creating a superuser

    def __str__(self):
        return self.email