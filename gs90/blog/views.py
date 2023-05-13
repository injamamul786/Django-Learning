from django.shortcuts import render, HttpResponse
from . import signals 
# Create your views here.
def home(request):
    signals.notification.send(sender=request.user, request=request,
                               user=["Injamam", "haq"])
    return HttpResponse("This is home page")