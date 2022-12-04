from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    like=models.ManyToManyField(User,related_name="like")

    def __str__(self):
        return self.title

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)

    def __str__(self):
        return self.comment
