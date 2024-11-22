from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Lower

class User(AbstractUser):
    pass

class Task(models.Model):
    taskName = models.CharField(max_length=255)
    description = models.TextField()
    users= models.ManyToManyField(User, related_name="tasks", through="UserTasks")
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='task_photos/%Y/%m/%d/', blank=True, null=True) #update to files
    
    class Meta:
        ordering = [Lower("taskName")]

class UserTasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]