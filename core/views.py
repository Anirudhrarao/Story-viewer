from turtle import ht
from django.shortcuts import render, redirect
from .models import ProfileUser, Status
from django.http import HttpResponse
import json
from .forms import AddStoryForm
# Create your views here.
def home(request):
    stories = []
    for user in ProfileUser.objects.all():
        items = []
        for status in user.status.all():
            items.append({
                "id": status.id,
                "type": "",
                "length": 3,
                "src": f'/media/{status.file}'
            })
        stories.append({
            "id": str(user.uid),
            "photo": f'/media/{user.photo}',
            "items": items,
            "name": user.name
        })

    return render(request,'home.html',context={'stories':json.dumps(stories)})

def addstory(request):
    if request.method == 'POST':
        form = AddStoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            return HttpResponse('Something Went Wrong')

    form = AddStoryForm()
    return render(request,'add.html',{'form':form})