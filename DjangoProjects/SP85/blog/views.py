from django.dispatch.dispatcher import Signal
from django.shortcuts import render, HttpResponse
from blog import signals
# Create your views here.
def home(request):
    signals.notification.send(sender=None, request=request, user=['karan', 'ventya'])
    return HttpResponse('This is Home page')