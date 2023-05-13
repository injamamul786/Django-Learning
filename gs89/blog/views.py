from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    a = 10/0
    return HttpResponse('Hello')