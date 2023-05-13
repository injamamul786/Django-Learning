from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print("I am view")
    return HttpResponse("This is home page")

def exception(request):
    print("I am Exception View")
    a = 10/0
    return HttpResponse("this is Exception page")

def user_info(request):
    print("I am user info View")
    context = {'name':'Injamam'}
    return TemplateResponse(request, 'user.html', context)