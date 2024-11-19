from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Lower

class User(AbstractUser):
    pass

class Task(models.Model):
    taskName = models.CharField(max_length=255)
    description = models.TextField()
    users= models.ManyToManyField(User, related_name="tasks")
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = [Lower("name")]