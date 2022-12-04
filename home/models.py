
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



    
class userprofile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE,related_name='User')
    firstname=models.CharField(blank=True,max_length=200)
    lastname=models.CharField(blank=True,max_length=200)
    email=models.EmailField(blank=True)
    profile_pic=models.ImageField(upload_to='profiles',default='profiles/img.jpg')
    followers=models.ManyToManyField(User,blank=True,related_name='followers')        
    following=models.ManyToManyField(User,blank=True,related_name='following')
    bio=models.CharField(max_length=200,blank=True)

class post_table(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE,max_length=200,blank=False)
   post_profile=models.ForeignKey(userprofile,on_delete=models.CASCADE)
   caption=models.CharField(max_length=200)
   postImage=models.ImageField(upload_to='posts',blank=False)
   upload_date=models.DateTimeField(auto_now_add=True)
   likes=models.ManyToManyField(User,blank=True,default=0,related_name='likes')
class comments(models.Model):
    post=models.ForeignKey(post_table,on_delete=models.CASCADE,related_name='post',default='')
    user=models.ForeignKey(userprofile,on_delete=models.CASCADE,related_name='user')
    comment=models.CharField(max_length=300,blank=False)
    date=models.DateTimeField(auto_now_add=True)

