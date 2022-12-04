# Generated by Django 3.2.15 on 2022-12-04 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='post',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='user',
        ),
        migrations.AddField(
            model_name='likes',
            name='likepost',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='likes',
            name='likeuser',
            field=models.CharField(default='', max_length=100),
        ),
    ]