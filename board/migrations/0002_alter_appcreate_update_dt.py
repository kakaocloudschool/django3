# Generated by Django 4.1.3 on 2022-11-29 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appcreate',
            name='update_dt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
