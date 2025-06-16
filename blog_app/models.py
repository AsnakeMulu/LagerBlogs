from django.contrib.auth.models import AbstractUser
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # Add extra fields (e.g., phone_number, profile_pic)

    USERNAME_FIELD = 'email'  # Login with email instead of username
    REQUIRED_FIELDS = ['username']  # Username still required but not for login

    def __str__(self):
        return self.email