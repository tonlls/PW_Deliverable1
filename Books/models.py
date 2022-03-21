# from calendar import c
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    decription = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    decription = models.TextField(max_length=1000,blank=True)
    website = models.URLField(max_length=200,blank=True)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    decription = models.TextField(max_length=1000,blank=True)
    website = models.URLField(max_length=200,blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    decription = models.TextField(max_length=1000,blank=True)
    website = models.URLField(max_length=200,blank=True)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    publishers = models.ManyToManyField(Publisher)
    pub_date = models.DateField()
    
    def __str__(self):
        return self.title