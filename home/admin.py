from django.contrib import admin
from home.models import Post,Category
# Register your models here.
admin.site.register((Post,Category))
