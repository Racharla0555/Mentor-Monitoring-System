from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    user=request.user
    if user.is_authenticated and mentors.objects.filter(user=user):
        st=mentors.objects.get(user=user)
    else:
        st=0
    return render(request,'home.html',{'st':st})
def view(r):
    user=r.user
    if user.is_authenticated and mentors.objects.filter(user=user):
        st=mentors.objects.get(user=user)
    else:
        st=0
    return render(r,'view.html',{'st':st})
import time
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        User.objects.create_user(username=username,email=email,password=password)
        time.sleep(3)
    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/view')
        else:
            messages.error(request,"Invalid login credentials")
    return render(request,'login.html')
def signout(request):
    logout(request)
    return redirect('home')
