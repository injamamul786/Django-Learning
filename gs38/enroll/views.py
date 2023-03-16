from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect 
# Create your views here.

def success(request):
    return render(request, 'enroll/success.html')

def showformdata(request):
    if request.method=="POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('form valid')
            print(fm.cleaned_data)
            print("name:", fm.cleaned_data['name'])
            print('email:', fm.cleaned_data['email'])
            print("mobile:", fm.cleaned_data['mobile'])
            print('password', fm.cleaned_data['password'])
            # return render(request, "enroll/success.html", {'name':fm.cleaned_data['name']})
            return HttpResponseRedirect("/reg/success/")
    else:
        fm = StudentRegistration()
    return render(request, "enroll/userregistration.html", {"form": fm})
