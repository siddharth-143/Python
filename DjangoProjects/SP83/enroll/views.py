from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
# def course(request):
#     mv = cache.get('movie', 'has_expired')
#     if mv == 'has_expired':
#         cache.set('movie', 'The Manjhi', 30)
#         mv = cache.get('movie')
#     return render(request, 'enroll/course.html', {'fm':mv})


# set and get cache in one line
# def course(request):
#     mv = cache.get_or_set('fees', 400, 30, version=2)
#     return render(request, 'enroll/course.html', {'fm':mv})


# setmany and getmany
# def course(request):
#     data = {'name':'karan', 'roll':101}
#     cache.set_many(data, 30)
#     sv = cache.get_many(data)
#     print(sv)
#     return render(request, 'enroll/course.html', {'stu':sv})


# delete
# def course(request):
#     cache.delete('fees', version=2)
#     return render(request, 'enroll/course.html')


# increment  and decresement
# def course(request):
#     dv = cache.decr('roll', delta=2)
#     print(dv)
#     cv = cache.incr('roll', delta=2)
#     print(cv)
#     return render(request, 'enroll/course.html')


# clear
def course(request):
    cache.clear()
    return render(request, 'enroll/course.html')