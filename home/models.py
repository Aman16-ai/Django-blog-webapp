from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH, AutoField
from froala_editor.fields import FroalaField
from django.contrib.auth.models import User
# Create your models here.
import datetime

class Category(models.Model):
    id = models.AutoField(primary_key= True)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="media/image")
    def __str__(self):
        return self.title
    
    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    img = models.ImageField(upload_to="media/image")
    content = FroalaField()
    date = models.DateField(default=datetime.date.today,null=True)
    category = models.ForeignKey(Category,on_delete=CASCADE,null=True)
    likes = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return  self.title
    
class likePost(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,null=True,blank=True ,on_delete=CASCADE)
    likecounts = models.IntegerField(null=True,blank=True)
    post = models.ForeignKey(Post,null=True,blank=True,on_delete=CASCADE)
    def __str__(self):
        return self.post
    
    
class ContactUsDetails(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50,blank=True,null=True)
    lastName = models.CharField(max_length=50,blank=True,null=True)
    email = models.CharField(max_length=50,blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    def __str__(self):
        return "Send by " + self.firstName + " " + self.lastName 
    
    
class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField(blank=True,null=True)
    post = models.ForeignKey(Post,on_delete=CASCADE)
    Reply = models.ForeignKey('self',on_delete=CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=CASCADE)
    date = models.DateField(default=datetime.datetime.today,null=True,blank=True)
    def __self__(self):
        return self.comment