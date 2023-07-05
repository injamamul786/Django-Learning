# from curses.ascii import HT
from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def app1(request):
    data = {'course':'Django framwork', 'website':'Instagram',"list":[1,2, 3, 4,5, 6, 7]}
    return render(request, 'temp_app1.html', {"appname":data})
