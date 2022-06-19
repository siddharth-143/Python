from django.shortcuts import render

# Create your views here.
def course(request):
    return render(request, 'enroll/course.html')

def contact(request):
    return render(request, 'enroll/contact.html')