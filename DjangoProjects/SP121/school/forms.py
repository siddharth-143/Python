from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=70)
    email = forms.EmailField(required=False)
    msg = forms.CharField(max_length=100, widget=forms.Textarea)

class FeedbackForm(forms.Form):
    your_name = forms.CharField(max_length=70)
    your_email = forms.EmailField(required=False)
    msg = forms.CharField(max_length=100, widget=forms.Textarea)