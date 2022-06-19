from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student

# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = 'school/student.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(course='python')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["freshers"] = Student.objects.all().order_by('name')
        return context
    
    def get_template_names(self):
        if self.request.COOKIES['user'] == "siddhya" :
            template_name = 'school/siddhya.html'
        else:
            template_name = self.template_name
        return[template_name]
        