from django.shortcuts import render, HttpResponseRedirect
from .forms import Signup, LoginForm, PostForm
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    post = Post.objects.all()
    return render(request, 'blog/home.html', {"posts":post})

#about
def about(request):
    return render(request, "blog/about.html")

#contact
def contact(request):
    return render(request, "blog/contact.html")
   

#dashborad
def userdashborad(request):
    if request.user.is_authenticated:
        post = Post.objects.all()
        return render(request, 'blog/dashborad.html', {'posts':post})
    else:
        return HttpResponseRedirect('/login/')
    

#signup
def signup(request):
    if request.method=='POST':
        fm = Signup(request.POST)
        if fm.is_valid():
            messages.success(request, 'Your account created successfully')
            user = fm.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            return HttpResponseRedirect('/dashborad/')
    else: 
        fm = Signup()
    return render(request, 'blog/signup.html', {'form':fm})

#login
def userlogin(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                pw = fm.cleaned_data['password']
                valid_user = authenticate(username=uname, password=pw)
                if valid_user is not None:
                    login(request, valid_user)
                    messages.success(request, "Login successefully")
                    return HttpResponseRedirect(f'/dashborad/')
        else:
            fm = LoginForm()
        return render(request, 'blog/login.html', {"form":fm})
    else:
        return HttpResponseRedirect('/dashborad/')
#logout
def userlogout(request):
    if request.user.is_authenticated:
        logout(request) 
    return HttpResponseRedirect('/')

#add
def addpost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm = PostForm(request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/dashborad/')
        else:
            fm = PostForm()
        return render(request, "blog/addpost.html", {"form":fm})
    else:
        return HttpResponseRedirect("/login/")
    

#update
def updatepost(request, id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi = Post.objects.get(pk=id)
            fm = PostForm(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/dashborad/')
        else:
            pi = Post.objects.get(pk=id)
            fm = PostForm(instance=pi)
        return render(request, "blog/update.html", {"form":fm})
    else:
        return HttpResponseRedirect("/login/")
    
def deletepost(request, id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect("/dashborad/")
    else:
        return HttpResponseRedirect("/login/")