from django.shortcuts import render


# Create your views here.
def settest(request):
    request.session.set_test_cookie()
    return render(request, 'student/settestcookie.html')


def checktest(request):
    name = request.session.test_cookie_worked()
    return render(request, 'student/checktestcookie.html', {'name':name})


def deltest(request):
    request.session.delete_test_cookie()
    return render(request, 'student/deltestcookie.html')

