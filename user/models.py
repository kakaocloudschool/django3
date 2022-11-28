from django.db import models

# Create your models here.

# user 모델
class User(models.Model):
    userid = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.TextField()
    privilege = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    