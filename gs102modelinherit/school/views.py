from django.shortcuts import render
from .models import Student, Teacher, Contractor
# Create your views here.

def home(request):
    st = Student.objects.all()
    t = Teacher.objects.all()
    con = Contractor.objects.all()
    return render(request, 'home.html', {'st': st, 't': t, 'con': con})
    