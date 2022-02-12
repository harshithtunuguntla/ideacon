import email
from turtle import title
from django.db import models

# Create your models here.


class ideas_store(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    handle = models.CharField(max_length=200)


    is_reviewd = models.BooleanField(default=False)

    def __str__(self):
         return self.title
    

class subscribe(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
         return self.email