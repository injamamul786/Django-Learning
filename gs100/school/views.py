from django.shortcuts import render
from .models import Student 
from django.db.models import Q
# Create your views here.
def home(request):
    # student_data = Student.objects.all()
    # student_data = Student.objects.filter(Q(id=6) & Q(roll=15))
    # student_data = Student.objects.filter(Q(name__iexact='salman') | Q(city__iexact='varanasi'))
    student_data = Student.objects.filter(~Q(roll=26))
    


    context = {'student':student_data,
               'sql_query':student_data.query 
               }

    return render(request, 'home.html', context)