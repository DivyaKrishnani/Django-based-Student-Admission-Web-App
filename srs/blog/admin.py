from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog.models import Post

admin.site.register(Post)
