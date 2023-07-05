from django.contrib import admin
from .models import Student, ExamCenter

# Register your models here.
@admin.register(ExamCenter)
class CenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','cname', 'city', 'name', 'roll']