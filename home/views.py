from typing import ContextManager
from django.http import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render,HttpResponse
from home.models import Post , Category ,likePost,ContactUsDetails,Comments
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from datetime import datetime
from home.fetchCategory import all_categories
# Create your views here.
def index(request):
    post = Post.objects.all()[::-1]
    category = all_categories()
    print(post)
    LatestPost = post[:4]
    print(LatestPost)
    context = {"post":LatestPost,"categories":category}
    return render(request,"index.html",context)

def blog(request):
    category = all_categories()
    post = Post.objects.all()[::-1]
    context = {"posts":post,"categories":category}
    return render(request,"blog.html",context)


def fullBlog(request,id):
    post = Post.objects.get(pk =id)
    print(post.img)
    allpost = Post.objects.all()
    comments = Comments.objects.filter(post = post)
    print(comments)
    blog_count = len(comments)
    context = {"post":post,"allpost":allpost,"comments":comments,"blog_count":blog_count}
    return render(request,'fullBlog.html',context)
    
def signupPage(request):
    return render(request,"signupPage.html")
  

def loginPage(request):
    return render(request,"newLoginPage.html")
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

def categoryPage(request,id):
    print(id)
    posts = Post.objects.filter(category=id)
    print(posts)
    context = {"posts":posts}
    return render(request,"categoryPage.html",context)


def searchBlog(request):
    if request.method == 'POST':
        query = request.POST['searchbox']
        print(query)
        posts = Post.objects.all()
        searchpostlst = []
        for p in posts:
            if query in p.title or query in p.content:
                searchpostlst.append(p)
            
        context = {"searchblogs":searchpostlst}
    return render(request,"searchpage.html",context)

def postliked(request,id):
    if request.method == 'POST':
        post = Post.objects.get(pk=id)
        print(post.likes)
    return HttpResponse(id)


def contactUsPage(request):
    return render(request,"contactus.html")

def handleContactus(request):
    if request.method == "POST":
        firstname = request.POST['firstNameIn']
        lastname = request.POST['lastNameIn']
        email = request.POST['emailIn']
        message = request.POST['messageTextarea']
        contact = ContactUsDetails(firstName = firstname,lastName = lastname,email= email,message = message )
        contact.save()
        
    return redirect('/')

def handlepostcommet(request,id):
    if request.method == 'POST':
        comment = request.POST['comment']
        post = Post.objects.get(pk=id)
        postcomment = Comments(comment = comment,user=request.user,post=post)
        postcomment.save()
        return redirect(f"/fullBlog/{id}")
    return HttpResponse("Something went wrong")