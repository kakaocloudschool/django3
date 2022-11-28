from django.db import models


# Create your models here.
class Cluster(models.Model):
    cluster_name = models.CharField(max_length=100, primary_key=True)
    cluster_type = models.CharField(max_length=100)
    kubeconfig = models.FileField(null=True, upload_to="")
    cluster_url = models.TextField()
    user_id = models.CharField(max_length=100)
    insert_date = models.DateTimeField(auto_now_add=True)
    bearer_token = models.TextField()