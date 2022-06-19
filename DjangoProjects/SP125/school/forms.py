from django import forms
from django.forms import widgets
from django.forms.models import model_to_dict
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        widgets = {'name': forms.TextInput(attrs={'class': 'myclass'}),
                   'password': forms.PasswordInput(render_value=True, attrs={'class': 'mypass'})}
