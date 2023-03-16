from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(initial="Injamamul", help_text="max character 30 is possible")
    email = forms.EmailField()
    first_name = forms.CharField()