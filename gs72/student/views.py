from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def setsession(request):
    # request.session['key'] = 'value'
    request.session['first'] = 'Muskan'
    request.session.set_expiry(10) #this time is in sec
    # request.session['secand'] = 'Akriti'
    return render(request, 'student/setsession.html')


def getsession(request):
    name = request.session["first"]
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date)
    print(request.session.get_expire_at_browser_close())
    return render(request, 'student/getsession.html', {'name':name})


def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')

