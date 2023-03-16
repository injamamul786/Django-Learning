from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(min_length=5, max_length=55, strip=False,
     error_messages={'required':'Enter your name'})
    roll= forms.IntegerField(min_value=0, max_value=100)
    price = forms.DecimalField(min_value=0, max_value=100, decimal_places=2, max_digits=5)
    rate = forms.FloatField(min_value=0, max_value=100)
    comment = forms.SlugField()
    email = forms.EmailField()
    website = forms.URLField()
    password = forms.CharField(widget=forms.PasswordInput())
    description = forms.CharField(widget=forms.Textarea)
    feedback = forms.CharField(widget=forms.TextInput(attrs={'class':'somecss1 somecss2', 'id':'uniqueid'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'row':3, 'col':50}))
    agree = forms.BooleanField(label="I Agree", label_suffix="")
