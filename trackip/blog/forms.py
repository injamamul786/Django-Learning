from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post
class Signup(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control cnt'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control cnt'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}
        widgets =  {'username':forms.TextInput(attrs={'class':'form-control cnt'}),
                    'first_name':forms.TextInput(attrs={'class':'form-control cnt'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control cnt'}),
                    'email':forms.EmailInput(attrs={'class':'form-control cnt'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control cnt', 'autofocus':True}))
    password = forms.CharField(label=_("Password"), strip=True,
                                widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 
                                                                  'class':'form-control cnt'}))
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc']
        labels = {'title':'title', 'desc':'Description'}
        widgets =  {'title':forms.TextInput(attrs={'class':'form-control cnt'}),
                    'desc':forms.Textarea(attrs={'class':'form-control cnt'})}