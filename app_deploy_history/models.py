from django.db import models

# Create your models here.
class App_deploy_history(models.Model):
    history_id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=100)
    revision = models.CharField(max_length=100)
    deploy_type = models.CharField(max_length=20)
    user_id = models.CharField(max_length=100)
    insert_dt = models.DateTimeField(auto_now_add=False)
    manager_id = models.CharField(max_length=100)
    manager_date = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)