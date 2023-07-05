from django.shortcuts import render
from .models import ExamCenter, MyExamCenter
# Create your views here.

def home(request):
    # st = Student.objects.all()
    ec = ExamCenter.objects.all()
    myec = MyExamCenter.objects.all()
    return render(request, 'home.html', {'exam':ec, 'myexam':myec})

    