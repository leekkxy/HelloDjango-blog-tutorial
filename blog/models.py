from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class Post(models.Model):
# name = models.CharField(max_length=100)
# text= models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    experct = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
