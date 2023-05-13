from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    print("I am view")
    return HttpResponse("This is home page")