from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=500)
    mobno = models.CharField(max_length=12, default='')
    email = models.EmailField(max_length=50, default='')
    mydoc = models.BooleanField(User,default=False)