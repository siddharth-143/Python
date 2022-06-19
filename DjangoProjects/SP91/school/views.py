from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q

# Create your views here.
def home(request):
    student_data = Student.objects.all()          # all method

    # student_data = Student.objects.filter(marks=89)         # filter method

    # student_data = Student.objects.exclude(marks=89)         # exclude method

    # student_data = Student.objects.order_by('marks')         # orde_by method
    # student_data = Student.objects.order_by('-marks')         # orde_by method
    # student_data = Student.objects.order_by('?')         # orde_by method
    # student_data = Student.objects.order_by('name')         # orde_by method

    # student_data = Student.objects.order_by('id').reverse()[:5]         # reverse method

    # student_data = Student.objects.values()        # value method
    # student_data = Student.objects.values('name', 'city')        # value method


    # student_data = Student.objects.values_list()        # value_list method
    # student_data = Student.objects.values_list('id', 'name')        # value_list method
    # student_data = Student.objects.values_list('id', 'name', named=True)        # value_list method

    # student_data = Student.objects.using('default')        # using method

    # student_data = Student.objects.dates('pass_date', 'year')        # dates method

################################### Teacher Table (Second Table) #################################

    # qs1 = Student.objects.values_list('id', 'name', named=True)           # union
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.union(qs1)

    # qs1 = Student.objects.values_list('id', 'name', named=True)           # union
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.union(qs1, all=True)

    # qs1 = Student.objects.values_list('id', 'name', named=True)           # intersection
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.intersection(qs1)

    # qs1 = Student.objects.values_list('id', 'name', named=True)           # difference
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.difference(qs1)

    ###################### AND OR Operator #################################

    # student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=106)
    # student_data = Student.objects.filter(id=6, roll=106)
    # student_data = Student.objects.filter(Q(id=6) & Q(roll=106))

    # student_data = Student.objects.filter(id=6) | Student.objects.filter(roll=107)
    student_data = Student.objects.filter(Q(id=6) | Q(roll=106))

    print("Return : ", student_data)
    print()
    print("SQL Query : ", student_data.query)
    return render(request, 'school/home.html', {'students':student_data})