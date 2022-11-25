from django.contrib.auth.models import User
from django.db import models


""" # 게시판 모델 삭제 예정
class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE) """
    
# HPA 스케줄러 모델
class Hpadata(models.Model):
    id = models.AutoField(primary_key=True)
    namespace = models.CharField(max_length=100)
    container = models.CharField(max_length=100)
    hpa = models.CharField(max_length=20)
    maxcpu = models.DecimalField(decimal_places=2, max_digits=5)
    maxram = models.DecimalField(decimal_places=2, max_digits=5)
    minrep = models.IntegerField()
    maxrep = models.IntegerField()
    autosche = models.BooleanField()
    promql = models.TextField()