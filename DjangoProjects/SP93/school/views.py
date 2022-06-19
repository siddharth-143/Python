from django.shortcuts import render
from .models import Student
from datetime import date, time

# Create your views here.
def home(request):
    # student_data = Student.objects.all()

    # student_data = Student.objects.filter(name__exact='karan')
    # student_data = Student.objects.filter(name__iexact='karan')
    # student_data = Student.objects.filter(name__contains='a')
    # student_data = Student.objects.filter(name__icontains='A')
    # student_data = Student.objects.filter(id__in=[1, 2, 3, 6])
    # student_data = Student.objects.filter(marks__in=[90])
    # student_data = Student.objects.filter(marks__gt=90)
    # student_data = Student.objects.filter(marks__gte=90)
    # student_data = Student.objects.filter(marks__lt=90)
    # student_data = Student.objects.filter(marks__lte=90)
    # student_data = Student.objects.filter(name__startswith='s')
    # student_data = Student.objects.filter(name__istartswith='S')
    # student_data = Student.objects.filter(name__endswith='a')
    # student_data = Student.objects.filter(name__iendswith='A')

    # student_data = Student.objects.filter(passdate__range=('2021-11-25', '2021-11-27'))
    # student_data = Student.objects.filter(admdatetime__date=date(2021,11,27))
    # student_data = Student.objects.filter(admdatetime__date__gt=date(2021,11,27))
    # student_data = Student.objects.filter(passdate__year=2021)
    # student_data = Student.objects.filter(passdate__year__gte=2020)
    # student_data = Student.objects.filter(passdate__month=11)
    # student_data = Student.objects.filter(passdate__month__gte=11)
    # student_data = Student.objects.filter(passdate__day=27)
    # student_data = Student.objects.filter(passdate__day__gte=27)                # greater than or equal to
    # student_data = Student.objects.filter(passdate__week=47)
    # student_data = Student.objects.filter(passdate__week__gt=47)
    # student_data = Student.objects.filter(passdate__week__gte=47)
    # student_data = Student.objects.filter(passdate__week_day=7)
    # student_data = Student.objects.filter(passdate__week_day__gt=7)
    # student_data = Student.objects.filter(passdate__week_day__gte=7)
    # student_data = Student.objects.filter(passdate__quarter=4)
    # student_data = Student.objects.filter(admdatetime__time__gt=time(12,30))
    # student_data = Student.objects.filter(admdatetime__hour__gte=12)
    # student_data = Student.objects.filter(admdatetime__minute__gte=30)
    student_data = Student.objects.filter(roll__isnull=False)


    print("Return : ", student_data)
    print()
    print('SQL Query : ', student_data.query)
    return render(request, 'school/home.html', {'students':student_data})