from django.shortcuts import render
from .models import Student, ExamCenter
# Create your views here.

def home(request):
    st = Student.objects.all()
    ec = ExamCenter.objects.all()
    return render(request, 'home.html',{'student':st, 'exam':ec})

    