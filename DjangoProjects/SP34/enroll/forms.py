from django import forms
from django.forms import widgets
from django.forms.fields import EmailField

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)