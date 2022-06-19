from django.contrib import admin
from enroll.models import Student

# Register your models here.

# register a site using decorator
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stuid', 'stuname', 'stuemail', 'stupass')


# admin.site.register(Student, StudentAdmin)