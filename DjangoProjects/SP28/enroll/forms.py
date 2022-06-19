from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(help_text="Hello how are you!!")
    email = forms.EmailField()
    mobile = forms.IntegerField()