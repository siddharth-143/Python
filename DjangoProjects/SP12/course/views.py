from django.shortcuts import render

# Create your views here.
def learn_django(request):
    return render(request, 'course/courseone.html', context={'title':'Learn Django', 'cname':'Django'})

def learn_python(request):
    return render(request, 'course/coursetwo.html', context={'title':'Learn Python', 'cname':'Python'})