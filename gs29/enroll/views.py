from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
    # fm = StudentRegistration(auto_id='some_%s', label_suffix='=', initial={ 'name':'sonam', 'email':'sonam@gmail.com'})
    # fm = StudentRegistration(auto_id=True)
    # fm = StudentRegistration(auto_id=False)

    fm = StudentRegistration()
    fm.order_fields(field_order=['email', 'first_name','name'])
    return render(request, 'enroll/userregistration.html', {"form":fm})