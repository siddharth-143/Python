from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    # student_data = Student.object.all()
    student_data = Student.student.get_stu_roll_range(101, 104)
    return render(request, 'school/home.html', {'students':student_data})