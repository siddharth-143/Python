from django.shortcuts import render

# Create your views here.


# set session
def setsession(request):
    request.session['name'] = 'karan'
    request.session['lname'] = 'rathod'
    return render(request, 'student/setsession.html')


# get a session
def getsession(request):
    name = request.session.get('name', default='Guest')
    lname = request.session.get('lname')
    keys = request.session.keys()
    items = request.session.items()
    # age = request.session.setdefault('age', '27')
    return render(request, 'student/getsession.html', {'name': name, 'keys': keys, 'lname': lname, 'items': items})


# delete a session
# def delsession(request):
#     if 'name' in request.session:
#         del request.session['name']
#     return render(request, 'student/delsession.html')


# delete a session using fluch() method
def delsession(request):
    request.session.flush()
    return render(request, 'student/delsession.html')

