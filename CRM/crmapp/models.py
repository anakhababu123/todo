from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dob=models.DateField(null=True)
    qualifiaction=models.CharField(max_length=200)
    image=models.ImageField(upload_to="image",null=True,blank=True)

    def __str__(self):
        return self.name

class Courses(models.Model):
    course_name=models.CharField(max_length=200)
    fees=models.PositiveIntegerField()
    duration=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.course_name


class Batches(models.Model):
    course=models.ForeignKey(Courses)
    batch_code=models.CharField(max_length=200,unique=True)
    started_date=models.DateField(null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.batch_code

class Placements(models.Model):
    student=models.ForeignKey(Students)
    company=models.CharField(max_length=200)
    dep=models.CharField(max_length=150)
    date=models.DateField(null=True)

class Batchstudent(models.Model):
    student=models.ForeignKey(Students,on_delete=models.CASCADE)
    batch=models.ForeignKey(Batches,on_delete=True)
