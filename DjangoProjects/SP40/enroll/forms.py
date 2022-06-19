from django import forms
from django.forms.widgets import PasswordInput


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Re-Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpwd = self.cleaned_data['password']
        valrpwd = self.cleaned_data['rpassword']
        if valpwd != valrpwd:
            raise forms.ValidationError('Password not match')
