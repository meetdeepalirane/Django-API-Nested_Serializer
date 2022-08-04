
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student,Department
from .serializers import StudentSerializer,DepartmentSerializer
from rest_framework import status
from rest_framework import viewsets



class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        print("******************List******************")
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Description:",self.description)

        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk=None):
        print("******************Retrieve******************")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)


        student_id=pk
        if student_id is not None:
            single=Student.objects.get(id=student_id)
            serializer=StudentSerializer(single)
            return Response(serializer.data)


    def create(self,request):
        new_student=StudentSerializer(data=request.data)
        if new_student.is_valid():
            new_student.save()
            return Response({'msg':'New Student created'},status=status.HTTP_201_CREATED)
        return Response(new_student.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        student_id=pk
        student_tobe_updated = Student.objects.get(id=student_id)
        updated_student=StudentSerializer(student_tobe_updated,data=request.data)
        if updated_student.is_valid():
            updated_student.save()
            return Response({'msg':"Updated student record"})
        return Response(updated_student.errors,status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self,request,pk):
        student_id=pk
        student_tobe_updated = Student.objects.get(id=student_id)
        updated_student=StudentSerializer(student_tobe_updated,data=request.data,partial=True)
        if updated_student.is_valid():
            updated_student.save()
            return Response({'msg':"Updated student record partially"})
        return Response(updated_student.errors)


    def destroy(self,request,pk):
        student_tobe_deleted=Student.objects.get(id=pk)
        student_tobe_deleted.delete()
        return Response({'msg':'Record deleted successfully!!'},status=status.HTTP_200_OK)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

