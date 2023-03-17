from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    name = forms.CharField(max_length=100, required=False) #if want to use like this we can use and priority of this attr is higher 
    class Meta:
        model = User
        # fields = ['name', 'email','password']
        fields = ['name','password', 'email'] #change order
        labels = {'name':'Enter Name', 'email':'Enter Email', 'password':'Enter Password'}
        help_text = {'name':'Enter Your Name'}
        error_messages = {'name':{'required':'Write Your Name'}, 'password':{'required':"Password is required"}, 'email':{'required':'Email is required'}}
        # error_messages = {'password':{'required':'Write your password'}}
        widgets = {'password':forms.PasswordInput(attrs={'placeholder':'Write Password'}), 
        'name':forms.TextInput(attrs={'class':'myclass', 
        'placeholder':'Your Name'}),}  