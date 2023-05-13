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
    # student_data = Student.objects.get(id=1)
    # student_data = Student.objects.get(name='Injamam') #give multiple value returned error
    
    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('name').first()

    # student_data = Student.objects.last()

    # student_data = Student.objects.latest('pass_date')

    # student_data = Student.objects.earliest('pass_date')

    # student_data = Student.objects.all()
    # print(student_data.exists())

    # student_data = Student.objects.all()
    # student = Student.objects.get(pk=1)
    # print(student_data.filter(pk=student.id).exists())

    # student_data = Student.objects.create(name='Samir', roll=54, city='Allahabad', pass_date='2023-04-03', marks=60)

    # student_data, created = Student.objects.get_or_create(name='Samir', roll=54, city='Allahabad', pass_date='2023-04-03', marks=60)
    # print(created)
    # student_data, created = Student.objects.get_or_create(name='Aman', roll=15, city='Allahabad', pass_date='2023-04-03', marks=60)
    # print(created)

    # student_data = Student.objects.filter(id=5).update(name='Naeem manhari', roll=38, marks=78)
    # student_data = Student.objects.filter(marks=89).update(marks=78, city='Pass')

    # student_data, created = Student.objects.update_or_create(id=7, name='haq',defaults={'name':'Raju',})
    # print(created)
    # student_data, created = Student.objects.update_or_create(roll=32,defaults={'name':'Javed','marks':98, 'pass_date':'2023-04-04'})
    # print(created)
    
    # objs = [
    #     Student(name='Asif', roll=2, city='Dubai', marks=88, pass_date='2023-04-05'),
    #     Student(name='Arif', roll=5, city='kanpur', marks=68, pass_date='2024-05-05'),
    #     Student(name='Atif', roll=7, city='lucknow', marks=58, pass_date='2024-08-15')
    # ]
    # student_data = Student.objects.bulk_create(objs)


    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = 'Bhul gya'
    # student_data = Student.objects.bulk_update(all_student_data, ['city'])

    # student_data = Student.objects.in_bulk([1,2]) #give only id meantion in list
    # print(student_data[1].name)
    # print(student_data[2].marks)

    # student_data = Student.objects.in_bulk([]) #give no object
    # student_data = Student.objects.in_bulk() # give all object


    # student_data = Student.objects.get(pk=17).delete() #delete single data given pk
    # student_data = Student.objects.filter(marks=60).delete()
    # student_data = Student.objects.all().delete()


    student_data = Student.objects.all()
    # print(len(student_data))
    # print(student_data.count())


    print(Student.objects.all().explain())

    print("---------------------")
    # print("Student Data", student_data)
    
    return render(request, 'home.html', {'student':student_data}) 