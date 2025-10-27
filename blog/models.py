from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    description = models.CharField(max_length=300, null=True)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images", null=True)
    created_at = models.DateTimeField(auto_now=True)
    