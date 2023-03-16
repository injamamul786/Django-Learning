from django import forms

class StudentRegistration(forms.Form):
    # name = forms.CharField(widget=forms.PasswordInput())
    # name = forms.CharField(widget=forms.HiddenInput())
    # name = forms.CharField(widget=forms.Textarea())
    # name = forms.CharField(widget=forms.CheckboxInput())
    # name = forms.CharField(widget=forms.FileInput())
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'classcss1'}))