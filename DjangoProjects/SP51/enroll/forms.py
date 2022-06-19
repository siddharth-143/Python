from django import forms
from django.db.models import fields
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['name', 'email', 'password']
        # fields = '__all__'
        exclude = ['password']