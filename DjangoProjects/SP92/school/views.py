from os import name
from django.shortcuts import render
from .models import Student

# Create your views here.


def home(request):
    # student_data = Student.objects.get(pk=1)            # get() method

    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('name').first()
    
    # student_data = Student.objects.last()           # last() method

    # student_data = Student.objects.latest('pass_date')           # latest() method

    # student_data = Student.objects.earliest('pass_date')           # earliest() method

    # student_data = Student.objects.all()
    # # print(student_data.exists())
    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.pk).exists())

    # student_data = Student.objects.create(name='sham', roll=113, city='solapur', marks=89, pass_date='2021-11-26')

    # student_data, created = Student.objects.get_or_create(name='sham', roll=113, city='solapur', marks=89, pass_date='2021-11-26')
    # print(created)

    # student_data = Student.objects.filter(id=15).update(name='kabir')
    # student_data = Student.objects.filter(marks=89).update(city='pass')

    # student_data = Student.objects.update_or_create(id=14, name='sama', defaults={'name':'samadhan'})

    # obj = [
    #     Student(name='kapil', roll=116, city='mohol', marks=65, pass_date='2021-11-26'),
    #     Student(name='ramesh', roll=117, city='pune', marks=55, pass_date='2021-11-25'),
    #     Student(name='dinesh', roll=118, city='pune', marks=95, pass_date='2021-11-26'),
    # ]
    # student_data = Student.objects.bulk_create(obj)

    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = 'washingtone'
    #     student_data = Student.objects.bulk_update(all_student_data, ['city'])

    # student_data = Student.objects.in_bulk([1, 2, 3])
    # print(student_data[1].name)
    # student_data = Student.objects.in_bulk([])
    # student_data = Student.objects.in_bulk()

    # student_data = Student.objects.get(pk=18).delete()
    # student_data = Student.objects.filter(marks=98).delete()
    # student_data = Student.objects.all().delete()

    student_data = Student.objects.all()
    print(student_data.count())


    print("Return : ", student_data)
    return render(request, 'school/home.html', {'student': student_data})
 