from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
class Signup(UserCreationForm):
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}


class EditUserProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login','is_active']
        labels = {'email':'Email'}