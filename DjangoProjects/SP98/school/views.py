from django.shortcuts import render
from .models import ExamCenter, Student

# Create your views here.
def home(request):
    exam_center = ExamCenter.objects.all()
    studetn_data = Student.objects.all()
    print(exam_center)
    print(studetn_data)
    return render(request, 'school/home.html', {'centers':exam_center, 'students':studetn_data})