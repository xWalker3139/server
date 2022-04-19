from django.db import models
from django.contrib.auth.models import User
import datetime

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    profile_pic = models.ImageField(null=True, blank=False, upload_to="images/", default="default")

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=264, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    description = models.TextField(max_length=10000, null=True, blank=False)
    date = models.DateField(auto_now_add=datetime.datetime.now(), null=True, blank=False)
    image = models.ImageField(null=True, blank=False, upload_to="images/")

    def __str__(self):
        return self.title

class Comment(models.Model):
    first_name = models.CharField(max_length=264, null=True, blank=False)
    last_name = models.CharField(max_length=264, null=True, blank=False)
    comment = models.TextField(max_length=10000, null=True, blank=False)

    def __str__(self):
        return self.first_name

# Create your models here.
