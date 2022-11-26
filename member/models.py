from django.db import models

# Create your models here.

# user 모델
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.TextField()
    auth = models.CharField(max_length=20)
    
    