from django.shortcuts import render
from .forms import Signup
from django.contrib import messages
# Create your views here.

def sign_up(request):
    if request.method=='POST':
        fm = Signup(request.POST)
        if fm.is_valid():
            messages.success(request, 'Your account created successfully')
            fm.save()

    else: 
        fm = Signup()
    return render(request, 'enroll/signup.html', {'form':fm})