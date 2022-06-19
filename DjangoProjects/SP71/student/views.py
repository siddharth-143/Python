from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


# set session
def setsession(request):
    request.session['name'] = 'karan'
    return render(request, 'student/setsession.html')


# get a session
def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True
        return render(request, 'student/getsession.html', {'name': name})
    else:
        return HttpResponse("<h1>You Session has Expired....</h1>")


# delete a session using fluch() method
def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')

