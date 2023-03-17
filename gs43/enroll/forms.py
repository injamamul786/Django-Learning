from django import forms

class StudentRegistration(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(15)])
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    rpassword = forms.CharField(widget=forms.PasswordInput(), label="Re-Enter Password")

    
    def clean(self):
        cleaned_data = super().clean()

        valpwd = self.cleaned_data['password']
        valrpwd = self.cleaned_data['rpassword']
        if valpwd!=valrpwd:
            raise forms.ValidationError('Password Not Matched')

        

