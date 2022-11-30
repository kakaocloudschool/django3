from django.db import models


""" # 게시판 모델 삭제 예정
class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE) """
    
# app 생성
class Appcreate(models.Model):
    app_name = models.CharField(max_length=100, primary_key=True)
    cluster_name = models.ForeignKey(
        "cluster.Cluster", related_name="cluster", on_delete=models.DO_NOTHING,
    )
    namespace = models.CharField(max_length=100)
    repo_url = models.TextField()
    target_revision = models.TextField()
    target_path = models.TextField()
    insert_dt = models.DateTimeField(auto_now_add=True)
    insert_user = models.CharField(max_length=100)
    update_dt = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=100)