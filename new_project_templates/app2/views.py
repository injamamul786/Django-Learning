from django.shortcuts import render

# Create your views here.
def app2(request):
    return render(request, 'temp_app2.html')

