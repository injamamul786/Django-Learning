from django.shortcuts import render
from .forms import StudentForm
from .models import User
# Create your views here


def show_details(request):
    if request.method=='POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentForm()
    return render(request, 'enroll/show.html', {'form':fm})

  