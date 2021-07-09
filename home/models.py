from django.db import models
from froala_editor.fields import FroalaField
# Create your models here.
import datetime
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    img = models.ImageField(upload_to="media/image")
    content = FroalaField()
    date = models.DateField(default=datetime.date.today,null=True)
    def __str__(self):
        return  self.title
    