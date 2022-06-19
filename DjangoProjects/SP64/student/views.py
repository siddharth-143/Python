from datetime import datetime, timedelta
from django.http import response
from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_cookie('name', 'karan', expires=datetime.utcnow()+timedelta(days=2))
    return response

def getcookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name')
    return render(request, 'student/getcookie.html', {'name':name})

def delcookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('name')
    return response