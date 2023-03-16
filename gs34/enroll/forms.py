from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(label='Your Name', label_suffix=' ', 
    initial='injamam', required=False, disabled=True,help_text='limit 70 char')
    