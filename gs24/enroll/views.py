from django.shortcuts import render
from enroll.models import Student
# Create your views here.

def studentinfo(request):
    
    student = Student(stuid=129, stuname='injamam', stuemail='injamam@gmail.com', stupass='1234')
    # student.save()
    stud = Student.objects.all()
    
    return render(request, 'enroll/studetail.html', {'stu':stud})
