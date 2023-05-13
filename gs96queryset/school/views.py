from django.shortcuts import render
from django.db.models import Q
# from .forms import StudentForm
from .models import Student
# Create your views here.
# def ragform(request):
#     if request.method=='POST':
#         fm = StudentForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#     else:
#         fm = StudentForm()
#     return render(request, 'form.html', {'form':fm})

def home(request):
    student_data = Student.objects.all()
    # student_data = Student.objects.filter(marks=89)

    # student_data = Student.objects.exclude(marks=89)

    # student_data = Student.objects.order_by('name') #return in assending order
    # student_data = Student.objects.order_by('-marks') #return in descending order (-)
    # student_data = Student.objects.order_by('?') #Give randomally
    # student_data = Student.objects.order_by('name') # order by name in ascending and Capital letter come first
    
    # student_data = Student.objects.order_by('id').reverse()
    # student_data = Student.objects.order_by('id').reverse()[:5]  
    # student_data = Student.objects.order_by('id').reverse()[2:5]

    # student_data = Student.objects.values()
    # student_data = Student.objects.values('name')
    # student_data = Student.objects.values('name', 'city')

    # student_data = Student.objects.distinct()

    # student_data = Student.objects.values_list()
    # student_data = Student.objects.values_list('name', 'marks')
    # student_data = Student.objects.values_list('name', 'roll', named=True)

    # student_data = Student.objects.using('default') #Write database name from setting.py

    # student_data = Student.objects.dates('pass_date', 'month')
    # student_data = Student.objects.dates('pass_date', 'year')

    # student_data = Student.objects.none()

    # student_data = Student.objects.union("other table name") 

    # student_data = Student.objects.intersection('other table name') 
    
    # student_data = Student.objects.diffrence('other table name')

    # student_data = Student.objects.filter(id=5) & Student.objects.filter(roll=22)
    # student_data = Student.objects.filter(id=5, roll=22)   
    # student_data = Student.objects.filter(Q(id=5) & Q(roll=22))

    # student_data = Student.objects.filter(id=5) | Student.objects.filter(roll=34)
    # student_data = Student.objects.filter(Q(id=5) | Q(roll=41))

    print("Student Data", student_data)
    print()
    print('SQL Query: ', student_data.query)
    return render(request, 'home.html', {'data':student_data})