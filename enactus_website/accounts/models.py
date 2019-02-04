from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=30,default='')
    position = models.CharField(max_length=15,default='')
    picture = models.ImageField(upload_to='images/',null=True,blank=True)
    details = models.CharField(max_length=100,null=True,blank=True)
    number = models.IntegerField(null=True)



