from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    # st = Student.objects.all()
    st = Student.student.all()
    return render(request, 'home.html', {'student':st})

    