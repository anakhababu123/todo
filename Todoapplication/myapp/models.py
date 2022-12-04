from django.db import models
from django.contrib.auth.models import User


# Create your models here.

todos=[

    {"id":1,"task_name":"gbillpay","user":"ram"},
    {"id":2,"task_name":"task2","user":"ravi"},
    {"id":3,"task_name":"task3","user":"arjun"},
    {"id":4,"task_name":"task4","user":"aravind"},
    {"id":5,"task_name":"task5","user":"arjun"},
    {"id":6,"task_name":"task6","user":"hari"},

    
]



class Todos(models.Model):
    task_name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.task_name


   



# orm query for creating an object
# ModelName.objects.create(fieldname=value1,field2=value2....fieldn=valuen)
# qs=modelname.objects.all()--listb all object
# t=modelname.objects.get(id=2)--get specific object
# td=modelname.obejects.filter(user="ram")--filtering
# Todos.objects.filter(id=1).update(task_name="electricity bill")--update
# Todos.objects.filter(id=2).delete