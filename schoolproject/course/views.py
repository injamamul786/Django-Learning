from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homePage(request):
    return HttpResponse('Home page') 

def learn_django(request):
    return HttpResponse('<h1>Hello World</h1>')
def learn_html(request):
    return HttpResponse('<a href="https://www.google.com/">Google</a>')
def learn_d2(request):
    a = 10+20
    return HttpResponse(a)
def learn_d1(request):
    return HttpResponse('Hello world it me I am Injamamul Haq')

def learn_d3(request):
    return HttpResponse('Yes I can enter in <a href="https://www.amazon.in/">Amazon</a>')