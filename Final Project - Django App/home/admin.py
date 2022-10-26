from django.contrib import admin
from .models import *

admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Profile)