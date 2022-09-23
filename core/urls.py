from sqlite3 import adapt
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.addstory,name="add")
]
