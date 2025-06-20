from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username']  

    def __str__(self):
        return self.email
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    caption = models.CharField(max_length=150, null=True, blank=True )
    slug = models.CharField(max_length=150, null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey('blog_app.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-created_at')
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"