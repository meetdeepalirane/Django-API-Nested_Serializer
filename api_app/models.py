from django.db import models

# Create your models here.


class drink(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)

    def __str__(self):
        return "% %s" %(self.name,self.description)