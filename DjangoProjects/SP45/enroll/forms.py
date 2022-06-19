from django import forms
from django.core import validators
from django.db.models import fields
from . models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {'name': 'Enter Name', 'email': 'Enter Email',
                  'password': 'Enter Password'}
        error_messages = {
            'name': {'required': 'Name is important'},
            'email': {'required': 'Email is important'},
            'password': {'required': 'Password is important'}
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'myclass', 'placeholder':'name'}),
            'email':forms.EmailInput(attrs={'placeholder':'Password'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Password'})
        }
