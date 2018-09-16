from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import  User_Info


class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('用户信息',  {'fields': ['username', 'password']}),
        ('个人信息',  {'fields': ['nick_name', 'email', 'mobile']}),
        ('状态',      {'fields': ['is_active']}),
        ('登录状态',  {'fields': ['date_joined', 'last_login']})
    ]

admin.site.register(User_Info,UserProfileAdmin)