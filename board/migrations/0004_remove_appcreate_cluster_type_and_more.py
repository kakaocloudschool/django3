# Generated by Django 4.1.3 on 2022-11-30 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0005_alter_cluster_kubeconfig'),
        ('board', '0003_appcreate_cluster_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appcreate',
            name='cluster_type',
        ),
        migrations.AlterField(
            model_name='appcreate',
            name='cluster_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cluster', to='cluster.cluster'),
        ),
    ]
