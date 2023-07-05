from django.contrib import admin
from .models import Student, ProxyStudent

# Register your models here.
@admin.register(Student)
class CenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']


@admin.register(ProxyStudent)
class ProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']