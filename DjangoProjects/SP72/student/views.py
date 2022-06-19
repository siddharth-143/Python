from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


# set session
def setsession(request):
    request.session['name'] = 'karan'
    return render(request, 'student/setsession.html')


# get a session
def getsession(request):
    name = request.session['name']
    return render(request, 'student/getsession.html', {'name': name})


# delete a session using fluch() method
def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')
