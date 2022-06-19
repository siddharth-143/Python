from django.shortcuts import render, resolve_url
from .forms import StudentRegistration, forms

# Create your views here.
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("Form validated")
            print("Name : ", fm.cleaned_data['name'])
            print("Email : ", fm.cleaned_data['email'])
            print("Password : ", fm.cleaned_data['password'])
            print("rpassword : ", fm.cleaned_data['rpassword'])
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})