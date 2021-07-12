from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def employee(request):
    return HttpResponse("this is employee patge")
def profile(request):
    return render(request,'employee/profile.html')