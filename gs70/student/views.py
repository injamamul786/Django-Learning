from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def setsession(request):
    # request.session['key'] = 'value'
    request.session['name'] = 'Sonam'
    return render(request, 'student/setsession.html')


def getsession(request):
    # name = request.session['name']
    name = request.session.get('name', 'Guest')
    return render(request, 'student/getsession.html', {'name':name})


def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'student/delsession.html')


 