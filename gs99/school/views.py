from django.shortcuts import render
from .models import Student
from django.db.models import Avg, Sum, Min, Max, Count
# Create your views here.
def home(request):
    student_data = Student.objects.all()
    avg = student_data.aggregate(Avg('marks'))
    sum = student_data.aggregate(Sum('marks'))
    min = student_data.aggregate(Min('marks'))
    max = student_data.aggregate(Max('marks'))
    count = student_data.aggregate(Count('marks'))



    print('-------*************-----------')
    context = {'student':student_data, 
               'sql_query':student_data.query, 
               'average':avg, 
               'Sum':sum, 'Max':max, 'Min':min, 'Count':count}

    return render(request, 'home.html', context)