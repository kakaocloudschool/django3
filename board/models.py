from django.contrib.auth.models import User
from django.db import models


""" # 게시판 모델 삭제 예정
class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE) """
    
# app 생성
class Appcreate(models.Model):
    appname = models.CharField(max_length=100, primary_key=True)
    cluster = models.CharField(max_length=100)
    cn_img = models.CharField(max_length=100)
    tag = models.CharField(max_length=20)
    kube_cfg = models.CharField(max_length=100)
    kube_mani = models.TextField()
    repo_url = models.TextField()
    ins_date = models.DateTimeField(auto_now_add=False)
    ins_id = models.CharField(max_length=100)
    up_date = models.DateTimeField(auto_now_add=True)
    up_id = models.CharField(max_length=100)
    
# 유저 정보와 생성 정보를 DB에 저장 후 출력
class Apphistory(models.Model):
    appname = models.CharField(max_length=100, primary_key=True)
    cluster = models.CharField(max_length=100)
    cn_img = models.CharField(max_length=100)
    tag = models.CharField(max_length=20)
    kube_cfg = models.CharField(max_length=100)
    kube_mani = models.TextField()
    repo_url = models.TextField()
    ins_date = models.DateTimeField(auto_now_add=False)
    ins_id = models.CharField(max_length=100)
    up_date = models.DateTimeField(auto_now_add=True)
    up_id = models.CharField(max_length=100)
    
class cluster(models.Model):
    ins_id = models.CharField(max_length=100)
    up_date = models.DateTimeField(auto_now_add=True)
    up_id = models.CharField(max_length=100)
    up_id = models.CharField(max_length=100)
    up_id = models.CharField(max_length=100)
    up_id = models.CharField(max_length=100)
                