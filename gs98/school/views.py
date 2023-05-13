from django.shortcuts import render
from .models import Student
from datetime import date, time
# Create your views here.
def home(request):
    student_data = Student.objects.all()
    # student_data = Student.objects.filter(name__exact='Injamam') # case sensitive
    # student_data = Student.objects.filter(name__iexact='imran') #case insensetive
    
    # student_data = Student.objects.filter(name__contains='ma')
    # student_data = Student.objects.filter(name__icontains='MA')

    # student_data = Student.objects.filter(id__in=[1,2,25])
    # student_data = Student.objects.filter(marks__in=[60, 98, 97, 86])

    # student_data = Student.objects.filter(marks__gt=60) #grt than
    # student_data = Student.objects.filter(marks__gte=80) #grater than eql to

    # student_data = Student.objects.filter(marks__lt=80) #less than
    # student_data = Student.objects.filter(marks__lte=80) #less than eql to

    # student_data = Student.objects.filter(name__startswith='n')

    # student_data = Student.objects.filter(name__istartswith='in')

    # student_data = Student.objects.filter(name__endswith='m')

    # student_data = Student.objects.filter(passdate__range=('2022-04-01','2024-04-03'))
    # student_data = Student.objects.filter(admdatetime__date=date(2023,4,5))
    # student_data = Student.objects.filter(admdatetime__date__gt=date(2022,4,5))
    # student_data = Student.objects.filter(admdatetime__date__gte=date(2022,4,5))
    # student_data = Student.objects.filter(passdate__year=2023)
    # student_data = Student.objects.filter(passdate__month__gt=3)
    # student_data = Student.objects.filter(passdate__day=5)
    # student_data = Student.objects.filter(passdate__day__gte=5)
    # student_data = Student.objects.filter(passdate__week=14)
    # student_data = Student.objects.filter(passdate__week_day=2)
    # student_data = Student.objects.filter(passdate__quarter=2)

    # student_data = Student.objects.filter(admdatetime__time__gte=time(6,00,00))
    # student_data = Student.objects.filter(admdatetime__hour__gte=6) #0-24
    # student_data = Student.objects.filter(admdatetime__minute__gte=6) #0-60
    # student_data = Student.objects.filter(admdatetime__second__gte=20)

    # student_data = Student.objects.filter(roll__isnull=False)





    print('-------*************-----------')
    # print('Student data:', student_data.query)
    return render(request, 'home.html', {'student':student_data, 'sql_query':student_data.query})