from django.contrib import admin
from .models import ExamCenter, MyExamCenter

# Register your models here.
@admin.register(ExamCenter)
class CenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']

@admin.register(MyExamCenter)
class MyCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']