from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass 
  

class Listings(models.Model):
    item_name = models.CharField(unique=False, max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255, default="", unique=False)
    price = models.IntegerField(max_length=14, null=False, blank=True, default=0)
    date_created = models.DateTimeField(auto_now=True)
    owner = models.CharField(unique=False, max_length=255)   

# class Bids(models.Model):
#     item_name = models.CharField(max_length=255)
#     # slug = models.SlugField(unique=True, max_length=255)
#     # date_created = models.DateTimeField(auto_now=True)
#     # owner = models.CharField(max_length=255)   


# class Comments(models.Model):
#     content = models.TextField()
#     # slug = models.SlugField(unique=True, max_length=255)
#     # item_name = item_name = models.CharField(max_length=255)
#     # date_created = models.DateTimeField(auto_now=True)
#     # owner = models.CharField(max_length=255) 