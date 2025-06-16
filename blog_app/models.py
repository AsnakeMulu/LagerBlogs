from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username']  

    def __str__(self):
        return self.email