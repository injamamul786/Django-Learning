from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect


# Create your views here.


def showformdata(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm =  fm.cleaned_data["name"]
            em = fm.cleaned_data["email"]
            pw = fm.cleaned_data['password']
            print(nm, em, pw)
            

    else:
        fm = StudentRegistration()
    return render(request, "enroll/userregistration.html", {"form": fm})
