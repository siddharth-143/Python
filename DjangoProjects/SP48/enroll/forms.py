from django import forms
from django.core import validators
from django.db.models import fields
from . models import User


class StudentRegistration(forms.ModelForm):
    name = forms.CharField(max_length=50, required=False)
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {'name': 'Enter Name', 'email': 'Enter Email',
                  'password': 'Enter Password'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'name'}),
        }
