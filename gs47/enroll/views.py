from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
from .models import User

# Create your views here.


def showformdata(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm =  fm.cleaned_data["name"]
            em = fm.cleaned_data["email"]
            pw = fm.cleaned_data['password']
            # reg = User(name=nm, email=em, password=pw) #insert
            # reg.save()
            # reg = User(id=1,name=nm, email=em, password=pw) #update id=1
            # reg.save()
            reg = User(id=2) #delete id=2
            reg.delete()

    else:
        fm = StudentRegistration()
    return render(request, "enroll/userregistration.html", {"form": fm})
