from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="blog_images")

