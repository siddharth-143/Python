from django import forms
from django.db.models import fields
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        widgets = {'name': forms.TextInput(attrs={'class': 'myclass'}),
                   'password': forms.PasswordInput(attrs={'class': 'mypass'})}