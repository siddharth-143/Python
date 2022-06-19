from django import forms
from django.forms import widgets
from django.forms.fields import EmailField


class StudentRegistration(forms.Form):
    name = forms.CharField(error_messages={'required': 'Enter you name'}, min_length=5, max_length=10, strip=True, empty_value='xyz')

    roll = forms.IntegerField(min_value=1, max_value=4)
    price = forms.DecimalField(min_value=1, max_value=4, max_digits=4, decimal_places=1)
    rate = forms.FloatField(min_value=1, max_value=4)
    comment = forms.SlugField()
    email = forms.EmailField(min_length=1, max_length=40)
    website = forms.URLField(min_length=1, max_length=40)
    password = forms.CharField(min_length=1, max_length=40, widget= forms.PasswordInput)
    description = forms.CharField(widget=forms.Textarea)
    feedback = forms.CharField(min_length=1, max_length=40, widget=forms.Textarea(attrs={'class':'somecss1 somecss2', 'id':'uniqueid'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':4}))

    agree = forms.BooleanField(label_suffix=' ', label='I agree')
