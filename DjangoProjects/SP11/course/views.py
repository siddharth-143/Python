from django.shortcuts import render

# Create your views here.


def learn_django(request):
    return render(request, 'course/courseone.html', context={'nm':'Django'})

def learn_python(request):
    return render(request, 'course/coursetwo.html', context={'nm':'Python'})
