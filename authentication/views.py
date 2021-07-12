# from django import http
from django import http
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
# Create your views here.
# sdata = User.objects.all()
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get("loginname")
        password = request.POST.get("loginpassword")
        User = auth.authenticate(username = username,password = password)
        if User is not None:
            login(request,User)
            return redirect('profile')
        else:
            return HttpResponse('username and password invalid')
    else:
        return render(request,'authentication/login.html')
def logout(request):
    return render(request,'authentication/logout.html')
def registeration(request):
    if request.method == "POST":
        username = request.POST.get('registername')
        password = request.POST.get('registerpassword')
        email = request.POST.get('registeremail')
        Passwordconfirmation = request.POST.get('confirmpassword')
        # userform = User(username = username,password = password)
        if password == Passwordconfirmation:
            # userform.save()
            if User.objects.filter(username = username).exists():
                return HttpResponse('username already exist')
            elif User.objects.filter(email = email).exists():
                return HttpResponse('email already exist')
            
            else:
                Userform = User.objects.create_user(username = username,password= password,email= email)
                Userform.save()
                redirect('home')
        else:
            return redirect('loginpage')
    else:
        return render(request,'authentication/registeration.html')
