from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib import messages
# Create your views here.

def regi(request):
    if request.method=='POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, 'Your Account successfully created')
            messages.info(request, 'Now you can login')
            fm = RegistrationForm()
    else:
        fm = RegistrationForm()

    return render(request, 'enroll/registration.html', {'form':fm})

