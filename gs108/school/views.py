from django.shortcuts import render
from .models import Student, ProxyStudent
# Create your views here.

def home(request):
    # st = Student.objects.all()
    # st = ProxyStudent.student.all() # execute without costom manager
    st = ProxyStudent.student.get_stu_roll_range(10, 30) #execute with costom manager
    return render(request, 'home.html', {'student':st})
