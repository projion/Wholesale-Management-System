from django.contrib import admin
from .models import User

# Register your models here.
class User_Info(admin.ModelAdmin):
    list_display = ['username','firstname', 'lastname', 'user_age', 'user_email', 'user_phone', 'user_address','profile_photo']
admin.site.register(User, User_Info)