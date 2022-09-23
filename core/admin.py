from re import S
from turtle import st
from django.contrib import admin
from .models import ProfileUser, Status
# Register your models here.
admin.site.register(ProfileUser)
admin.site.register(Status)