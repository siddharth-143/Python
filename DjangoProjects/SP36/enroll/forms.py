from django import forms
from django.forms import widgets
from django.forms.fields import EmailField


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(min_length=1, max_length=40, widget= forms.PasswordInput)

    def clean_name(self):
        valname = self.cleaned_data['name']                     # valname = self.cleaned_data.get('name')
        if len(valname) < 4:
            raise forms.ValidationError('Enter more than or equal 4 char')
        return valname

