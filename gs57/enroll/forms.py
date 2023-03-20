from django import forms
from .models import User
class Registration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['st_name','email','password']
    
class TecherRegistration(Registration):
    class Meta(Registration.Meta):
        fields = ['tc_name', 'email','password']
