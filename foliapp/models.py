from django.db import models
from django.forms import ImageField

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='foliapp/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='foliapp/images')

    def __str__(self):
        return self.title

class About(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description

