from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(reques):
    return HttpResponse("<h1>Hello Django</h1>")