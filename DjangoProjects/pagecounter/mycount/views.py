from django.shortcuts import render

# Create your views here.
def mycount(request):
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    return render(request, 'mycount/mycount.html', {'c':newcount})