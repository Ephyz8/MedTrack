from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cadre = models.CharField(max_length=255, choices=[('user', 'Medical Equipment User'), ('engineer', 'Biomedical Engineer')])

    def __str__(self):
        return f"{self.username} ({self.email})"
