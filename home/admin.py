from typing_extensions import Concatenate
from django.contrib import admin
from home.models import Post,Category,ContactUsDetails,Comments
# Register your models here.
admin.site.register((Post,Category,ContactUsDetails,Comments))
