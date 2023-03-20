from django.shortcuts import render
from .models import User
from .forms import Registration,TecherRegistration
# Create your views here.
def student_form(request):
    if request.method=='POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = Registration()
    return render(request,'student.html', {'form':fm})

def teacher_form(request):
    if request.method=='POST':
        fm = TecherRegistration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=TecherRegistration()
    return render(request, 'teacher.html', {'form':fm})