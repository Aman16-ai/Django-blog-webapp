from typing import ContextManager
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from home.models import Post
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    post = Post.objects.all()[::-1]
    print(post)
    LatestPost = post[:4]
    print(LatestPost)
    context = {"post":LatestPost}
    return render(request,"index.html",context)

def blog(request):
    post = Post.objects.all()[::-1]
    context = {"posts":post}
    return render(request,"blog.html",context)


def fullBlog(request,id):
    post = Post.objects.get(pk =id)
    print(post.img)
    allpost = Post.objects.all()
    context = {"post":post,"allpost":allpost}
    return render(request,'fullBlog.html',context)
    
def signupPage(request):
    return render(request,"signupPage.html")
  

def loginPage(request):
    return render(request,"loginPage.html")
def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['Username_login']
        password = request.POST['pass_login']
        user = authenticate(username=username,password=password)
        if(user!=None):
            login(request,user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("Invalid credentials")

def handlesignup(request): 
    if request.method == "POST":
        username = request.POST['Username']
        firstname = request.POST['Firstname']
        lastname = request.POST['Lastname']
        email = request.POST['email']
        password = request.POST['pass']
        user = User.objects.create_user(username,email,password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
    
    return HttpResponseRedirect("/")

def handlelogout(request):
    user = logout(request)
    return HttpResponseRedirect("/")