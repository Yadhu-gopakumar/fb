# Generated by Django 3.2.15 on 2022-11-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='profiles/img.jpg', upload_to='profiles'),
        ),
    ]
