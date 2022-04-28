from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField, TimeField
import datetime
# Create your models here.
import os
from django.contrib.auth.models import User

class Chat_Groups(models.Model):
    name=models.CharField(max_length=50)
    members=models.IntegerField()
    user=models.ManyToManyField(User, null=True)
    
    def __str__(self):
        return(self.name)

class profile_details(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imgp=models.FileField(upload_to='imgs',default='default.jpg', null=True,blank=True)
    u_nm=models.CharField(max_length=150)
    fstname=models.CharField(max_length=250)
    secname=models.CharField(max_length=250)
    terimail=models.EmailField()
    fbacc=models.CharField(max_length=250)
    unicode = models.CharField(max_length=100,null=True)
    timestamp = models.DateTimeField(null=True)
    verified = models.BooleanField(default=False)

class Chat(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    group=models.ForeignKey(Chat_Groups,on_delete=models.CASCADE)
    message=models.CharField(max_length=200)
    timestamp=models.DateTimeField(null=True)

    def __str__(self):
        return(self.message)
