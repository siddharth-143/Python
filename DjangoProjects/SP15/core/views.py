from django.shortcuts import redirect, render

# Create your views here.
def home_page(request):
    return render(request, 'core/home.html')

def about_page(request):
    return render(request, 'core/about.html')