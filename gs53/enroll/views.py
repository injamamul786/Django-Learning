from django.shortcuts import render

# Create your views here

def home(request, check):

    return render(request, "enroll/home.html", {'check':check})

# def show_details(request, my_id):
#     return render(request, 'enroll/show.html', {'id':my_id})


def show_details(request, my_id=1): 
    if my_id==1:
        student = {'id':my_id, 'name':'injamam'}
    if my_id==2:
        student = {'id':my_id, 'name':'Imran'}
    if my_id==3:
        student = {'id':my_id, 'name':'Talib'}
    
    return render(request, 'enroll/show.html', student)


def show_subdetails(request, my_id=1, my_subid=5): 
    if my_id==1 and my_subid==5:
        student = {'id':my_id, 'name':'injamam', 'info':"sub details"}
    if my_id==2 and my_subid==6:
        student = {'id':my_id, 'name':'Imran', 'info':"sub details"}
    if my_id==3 and my_subid==7:
        student = {'id':my_id, 'name':'Talib', 'info':"sub details"}
    
    return render(request, 'enroll/show.html', student)
