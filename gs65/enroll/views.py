from django.shortcuts import render, HttpResponseRedirect
from .forms import Signup, EditUserProfile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.

#Sign up
def sign_up(request):
    if request.method=='POST':
        fm = Signup(request.POST)
        if fm.is_valid():
            messages.success(request, 'Your account created successfully')
            fm.save()
            return HttpResponseRedirect(f'/profile/{request.user}/')

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
        if request.method=='POST':
            fm = EditUserProfile(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, 'Edit successfully')
                fm.save()
        else:
            fm = EditUserProfile(instance=request.user)
        return render(request, 'enroll/profile.html', {'name':request.user, "form":fm})
    else:
        return HttpResponseRedirect('/login/')
    
#Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


#Change Password with old password
def changePass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect(f'/profile/{fm.user}/')
        else:
            fm  = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')

#without old password change password
def changePass1(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect(f'/profile/{fm.user}/')
        else:
            fm  = SetPasswordForm(user=request.user)
        return render(request, 'enroll/changepassword.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')