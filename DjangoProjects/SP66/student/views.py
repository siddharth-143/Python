from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'karan'
    request.session['lname'] = 'rathod'
    return render(request, 'student/setsession.html')

def getsession(request):
    # name = request.session['name']
    name = request.session.get('name', default='Guest')
    lname = request.session.get('lname')
    return render(request, 'student/getsession.html', {'name':name, 'lname':lname})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'student/delsession.html')