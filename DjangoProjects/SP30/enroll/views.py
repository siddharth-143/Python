from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showformdata(request):
    fm = StudentRegistration(initial={'name':'camlin'})
    return render(request, 'enroll/userregistration.html', {'form':fm})