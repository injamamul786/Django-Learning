from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def setcookie(request):
    response = render(request, 'student/setcookie.html')
    # response.set_cookie('name', 'django')
    # response.set_cookie('name', 'django', max_age=20)
    # response.set_cookie('name', 'django', expires=datetime.utcnow()+timedelta(days=2))
    # response.set_cookie('name', 'python')
    response.set_cookie('language', 'python')
    return response


def getcookie(request):
    # name = request.COOKIES['name']
    # name = request.COOKIES.get('name')
    # name = request.COOKIES.get('name', 'Guest')
    name = request.COOKIES.get('language', 'Guest')
    return render(request, 'student/getcookie.html', {'cookie':name})


def delcookie(request):
    responce = render(request, 'student/delcookie.html')
    responce.delete_cookie('name')
    return responce


