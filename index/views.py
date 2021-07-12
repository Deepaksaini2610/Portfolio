from django.shortcuts import render
from django.http import HttpResponse
from index.models import about
from index.models import slider
# Create your views here.
from django.shortcuts import render
def home(request):
    slidedata = slider.objects.all()
    aboutdata = about.objects.all()[0]
    simpledata = {
        'name':aboutdata,
        'slider':slidedata
    }
    return render(request,'index.html',simpledata)
def aboutus(request):
    return render(request,'about.html')
