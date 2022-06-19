from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'class':'somecss1', 'id':'uniqueid'}))