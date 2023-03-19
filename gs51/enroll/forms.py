from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    name = forms.CharField(max_length=100, required=False) 
    class Meta:
        model = User
        fields = ['name', 'email','password']
        labels = {'name':'Enter Name', 'email':'Enter Email', 'password':'Enter Password'}
        error_messages = {'name':{'required':'Write Your Name'}, 'password':{'required':"Password is required"}, 'email':{'required':'Email is required'}}
        widgets = {'password':forms.PasswordInput()}