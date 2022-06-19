from django.shortcuts import render

# Create your views here.


# set session
def setsession(request):
    request.session['name'] = 'karan'
    request.session.set_expiry(0)
    return render(request, 'student/setsession.html')


# get a session
def getsession(request):
    name = request.session['name']
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request, 'student/getsession.html', {'name': name})


# delete a session using fluch() method
def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')

