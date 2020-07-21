from django.db import models

# Create your models here.

class Book(models.Model):
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.CharField(max_length=13)
    quan = models.IntegerField()
