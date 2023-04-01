from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.
def setsession(request):
    # request.session['key'] = 'value'
    request.session['first'] = 'Muskan'
    # request.session.set_expiry(10) #this time is in sec
    # request.session['secand'] = 'Akriti'
    return render(request, 'student/setsession.html')


def getsession(request):
    if 'first' in request.session:
        name = request.session["first"]
        request.session.modified = True 
        return render(request, 'student/getsession.html', {'name':name})
    else:
        return HttpResponse('Your Session expired')

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')

