# Generated by Django 4.1.3 on 2022-11-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.TextField()),
                ('auth', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
