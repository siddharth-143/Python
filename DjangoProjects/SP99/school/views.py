from django.shortcuts import render
from .models import ExamCenter, MyExamCenter

# Create your views here.
def home(request):
    exam_center = ExamCenter.objects.all()
    my_center = MyExamCenter.objects.all()
    return render(request, 'school/home.html', {'centers':exam_center, 'mycenters':my_center})