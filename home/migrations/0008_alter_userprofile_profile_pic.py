# Generated by Django 3.2.15 on 2022-11-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20221128_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='img.jpg', upload_to='profiles'),
        ),
    ]
