# Generated by Django 3.2.15 on 2022-11-24 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_alter_userprofile_uploads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='uploads',
        ),
        migrations.RemoveField(
            model_name='post_table',
            name='likes',
        ),
        migrations.AddField(
            model_name='post_table',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post_table',
            name='post_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userprofile'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='followers',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='following',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
