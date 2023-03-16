from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(initial="injamam", help_text="enter valid text")
    email = forms.EmailField(initial="injamam@gmail.com", help_text="enter valid email")
    first_name = forms.CharField(initial="inja", help_text="enter only first name")