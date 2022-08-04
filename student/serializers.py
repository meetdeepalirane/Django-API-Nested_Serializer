from .models import Student,Department
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','Address','department']


class DepartmentSerializer(serializers.ModelSerializer):
    student_list=StudentSerializer(many=True,read_only=True)
    class Meta:
        model=Department
        fields=['id','dept_name','student_list']





