from django.shortcuts import render

# Create your views here.
def course(request):
    fm = 'Hello World'
    return render(request, 'enroll/course.html', {'fm':fm})
