from django.utils import timezone
from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.title