from django.db import models
from django.utils import timezone

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Your Name")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title