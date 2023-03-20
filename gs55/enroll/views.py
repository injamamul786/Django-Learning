from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here


def homepage(request):
    return render(request, "enroll/base.html")

def addandshow(request):
    
    if request.method=='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # fm.save() #simple method 
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            st = User(name=nm, email=em, password=pw)
            st.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, "enroll/addandshow.html", {'form':fm,'student':stud})

def delete_data(request, id):
    if request.method=='POST':
        data = User.objects.get(pk=id)
        data.delete()
    return HttpResponseRedirect('/addshow/')



def update(request, id):
    
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/addshow/')
    else:
        pi = User.objects.get(pk=id) 
        fm = StudentRegistration(instance=pi)

    return render(request, "enroll/updatestudent.html",{'form':fm})