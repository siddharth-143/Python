from django.shortcuts import render

# Create your views here.


def fees_django(request):
    return render(request, 'fees/feesone.html', context={'fn':'10000'})


def fees_python(request):
    return render(request, 'fees/feestwo.html', content={'fn':'20000'})
