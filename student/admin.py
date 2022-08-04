from django.contrib import admin
from .models import Student,Department
# Register your models here.
@admin.register(Department)
class DeptAdmin(admin.ModelAdmin):
    list_display = ['id','dept_name']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','Address','department']