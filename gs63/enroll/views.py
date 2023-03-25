from django.shortcuts import render, HttpResponseRedirect
from .forms import Signup
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

#Sign up
def sign_up(request):
    if request.method=='POST':
        fm = Signup(request.POST)
        if fm.is_valid():
            messages.success(request, 'Your account created successfully')
            fm.save()

    else: 
        fm = Signup()
    return render(request, 'enroll/signup.html', {'form':fm})

#login
def userLogin(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                pw = fm.cleaned_data['password']
                valid_user = authenticate(username=uname, password=pw)
                if valid_user:
                    login(request, valid_user)
                    messages.success(request, "Login successefully")
                    return HttpResponseRedirect(f'/profile/{uname}/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {"form":fm})
    else:
        return HttpResponseRedirect(f'/profile/{request.user}/')

#Profile
def profile(request, username):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/login/')
#Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

