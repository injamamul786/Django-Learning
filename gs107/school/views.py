from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    # st = Student.objects.all()
    st = Student.student.get_stu_roll_range(12, 30)
    return render(request, 'home.html', {'student':st})

    