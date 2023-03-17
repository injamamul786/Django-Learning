from django import forms
from django.core import validators

def start_with_s(value):
    if value[0].upper()!='S':
        raise forms.ValidationError("Name should be start with S")
def email_with_name(value):
    if value[-3:] !='com':
        raise forms.ValidationError("Email should be contain 'com' ")

class StudentRegistration(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(15)])
    name = forms.CharField(validators=[start_with_s])
    email = forms.EmailField(validators=[email_with_name])
    