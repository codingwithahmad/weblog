from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    STATUS_CHOICES = [
        ('p', 'Publish'),
        ('d', 'Draft')
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
