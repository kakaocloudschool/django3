# Generated by Django 4.1.3 on 2022-11-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cluster',
            fields=[
                ('cluster_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('cluster_type', models.DateTimeField(auto_now_add=True)),
                ('kubeconfig', models.CharField(max_length=100)),
                ('cluster_url', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('insert_date', models.CharField(max_length=100)),
            ],
        ),
    ]
