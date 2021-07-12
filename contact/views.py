from django.shortcuts import render
from contact.models import contact
# Create your views here.
def contactus(request):
    # contactdata = contact.objects.all()
    if request.method == 'POST':
        fName = request.POST.get('fname')
        lName = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        contactdetail = contact(fName=fName,lName=lName,phone = phone,email = email)
        contactdetail.save()
    return render(request,'contact.html')
