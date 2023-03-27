from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_signed_cookie('language', 'python', salt='name', expires=datetime.utcnow()+timedelta(days=2))
    return response


def getcookie(request):
    name = request.get_signed_cookie('language', 'Guest', salt='name')
    return render(request, 'student/getcookie.html', {'cookie':name})


def delcookie(request):
    responce = render(request, 'student/delcookie.html')
    responce.delete_cookie('name')
    return responce


