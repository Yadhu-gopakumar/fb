from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import post_table,userprofile,comments
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .form import profileform
from django.contrib import messages
# Create your views here.
@login_required(login_url='auth/')
def home(request):
    post=post_table.objects.all() 
    current=request.user
    
    try:
        currentuser=userprofile.objects.get(username=current)
        context={
        'posts':post,
        'userprofile':currentuser,  
         }
        return render(request,'feed.html',context)
     
    except:
        currentuser=userprofile.objects.create(username=current)
        context={
        'posts':post,
        'userprofile':currentuser,
         }
        return render(request,'feed.html',context)
       

       
# Create your views here.
@login_required(login_url='auth/')
def profile(request,user):
    userdata=userprofile.objects.get(username__username=user)
    comment=comments.objects.all()
    current=request.user
    currentuser=userprofile.objects.get(username=current)
    
    posts=post_table.objects.filter(user__username=user).all()
    if currentuser.following.filter(id=userdata.id).exists():
        isfollowing=True
    else:
        isfollowing=False    
    context={
        'profile_data':userdata,
        'userprofile':currentuser,
        'posts':posts,
        'comments':comment,
        'isfollowing':isfollowing
    }
    return render(request,'profile.html',context)   

@login_required(login_url='auth/')
def addpost(request):
    post=post_table.objects.all()
    current=request.user
    currentuser=userprofile.objects.get(username=current)
    context={
        'posts':post,
        'userprofile':currentuser,
        }
    if request.method=='POST':
        postImage=request.FILES['image']    
        caption=request.POST['caption']    
        user=request.user
        post_profile=userprofile.objects.get(username__username=user)
        print(post_profile)
        upload=post_table.objects.create(user=user,post_profile=post_profile,caption=caption,postImage=postImage)
        print('upload')
        upload.save()
        return redirect('/')    
        
    
    return render(request,'feed.html',context)    

@login_required(login_url='auth/')
def edit(request):
    # userdata=userprofile.objects.get(username__username=user)
   
    post=post_table.objects.all()
 
    current=request.user
    currentuser=userprofile.objects.get(username=current)
    # edituser_instance=userupdateform(request.POST or None,instance=current)
    edit_instance=profileform(request.POST or None, request.FILES or None,instance=currentuser)

    context={
        'posts':post,
        'userprofile':currentuser,
        'form':edit_instance,
         }
    if edit_instance.is_valid():
        
        edit_instance.save()
        return render(request,'feed.html',context)


    return render(request,'profileupdate.html',context)

@login_required(login_url='auth/')
def search(request):
    currentuser=userprofile.objects.get(username=request.user)
    context={
                'userprofile':currentuser,
                'data':'',
         
                    }
  
    if 'query' in request.GET:
        q=request.GET['query']
        # uname=User.objects.filter(username__icontains=q)

        res=userprofile.objects.filter(firstname__icontains=q) | userprofile.objects.filter(lastname__icontains=q) | userprofile.objects.filter(username__username__icontains=q)
   
        if res is not None:
            context={
                'userprofile':currentuser,
                'data':res,
                # 'uname':uname
                    }
        else:
            context={
            'userprofile':currentuser,
            'data':res,
                    }  
        return render(request,'search.html',context)
                    
    return render(request,'search.html',context)

@login_required(login_url='auth/')
def like(request,id):
    currentuser=request.user.id
    postid=id
    postinstance=post_table.objects.get(id=postid)
    if  postinstance.likes.filter(id=currentuser).exists():
        postinstance.likes.remove(request.user)
        postinstance.save()
        print('disliked')
        return redirect('/')
    else:
        postinstance.likes.add(request.user)
        postinstance.save()
        print('liked')
        return redirect('/')


    

def follow(request,user):
    userdata=userprofile.objects.get(username__username=user)
    comment=comments.objects.all()
    current=request.user
    currentuser=userprofile.objects.get(username=current)
    
    posts=post_table.objects.filter(user__username=user).all()
    if currentuser.following.filter(id=userdata.id).exists():
        currentuser.following.remove(userdata.id)
        isfollowing=False
    else:
        currentuser.following.add(userdata.id)
        isfollowing=True
        
    
    context={
        'profile_data':userdata,
        'userprofile':currentuser,
        'posts':posts,
        'comments':comment,
        'isfollowing':isfollowing
    }
    return render(request,'profile.html',context)
  

      
def comment(request,id):
    post=post_table.objects.get(id=id)
    currentuser=userprofile.objects.get(username=request.user)
    postcomments=comments.objects.filter(post=post)
    context={
        'comments':postcomments,
        'userprofile':currentuser,
        'posts':post,
    }

    if request.method=='POST':
        comment=request.POST['comment']
        commentinstance=comments.objects.create(post=post,user=currentuser,comment=comment)
        commentinstance.save()

    return render(request,'comments.html',context)  

def deletecomment(request,id):
    commentinstance=comments.objects.get(id=id)
    
    currentuser=userprofile.objects.get(username=request.user)
  
    postcomments=comments.objects.filter(post=commentinstance.post)

    post=commentinstance.post
    commentinstance.delete()
    context={
    'comments':postcomments,
    'userprofile':currentuser,
    'posts':post,
    }
    return render(request,'comments.html',context)  
    