from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.
def regi(request):
    messages.info(request, 'Now you can Login !!!')
    messages.success(request, 'Login Successfully !!!')
    messages.warning(request, 'Login Warning !!!')
    messages.error(request, 'Login Error !!!')

    fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})