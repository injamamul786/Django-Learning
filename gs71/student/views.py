from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def setsession(request):
    # request.session['key'] = 'value'
    request.session['first'] = 'Muskan'
    request.session['secand'] = 'Akriti'
    return render(request, 'student/setsession.html')


def getsession(request):
    # name = request.session['name']
    name = request.session.get('first', 'Guest')
    # keys = request.session.keys()
    items = request.session.items()
    # age = request.session.setdefault('age', '22')
    return render(request, 'student/getsession.html', {'name':name, 'items':items})


def delsession(request):
    # if 'first' in request.session:
    #     del request.session['first']
        # del request.session['second']
    request.session.flush()
    return render(request, 'student/delsession.html')


 