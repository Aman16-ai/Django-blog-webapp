from django.db import models
from django.db.models.deletion import CASCADE
from froala_editor.fields import FroalaField
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
    def __str__(self):
        return  self.title
    