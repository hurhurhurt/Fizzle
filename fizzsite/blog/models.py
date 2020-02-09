from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Quiz(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    pic = models.FileField(upload_to='media/images', default= None)
    interests = models.CharField(max_length=50)