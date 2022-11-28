from django.db import models

# Create your models here.
class cluster(models.Model):
    cluster_name = models.CharField(max_length=100, primary_key=True)
    cluster_type = models.DateTimeField(auto_now_add=True)
    bearer_token = models.TextField()
    kubeconfig = models.CharField(max_length=100)
    cluster_url = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    insert_date = models.CharField(max_length=100)