from django.contrib import admin

# Register your models here.
from django.contrib import admin
from reg.models import RegisterUser

admin.site.register(RegisterUser)
