from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(label='Your name', label_suffix=" ", initial='xyz', help_text="Limit 70 char", disabled=True)