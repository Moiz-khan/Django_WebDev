from django.shortcuts import render, HttpResponse
from .models import BlogPost
# Create your views here.
import requests
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm


def registerpage(request):
    form = CreateUserForm()

    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context  = {'form': form}
    return render(request, 'blog/register.html', context)


def index(request):
    myposts= BlogPost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html',{"mypost":myposts})


def blogpost(request, id):
    post = BlogPost.objects.filter(post_id=id)[0]
    print(post)

    return render(request, 'blog/blogpost.html', {"post": post})

    


