from django.db import models

# Create your models here.


class Department(models.Model):
    dept_name=models.CharField(max_length=100)

    def __str__(self):
        return "%s" %(self.dept_name)


class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    Address=models.CharField(max_length=50)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='student_list')

    def __str__(self):
        return "%s %s %s %s"%(self.name,self.roll,self.Address,self.department)