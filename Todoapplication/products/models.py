from email.policy import default
from random import choices
from django.db import models

# Create your models here.
class Mobiles(models.Model):
    name=models.CharField(max_length=200)
    brand=models.CharField(max_length=150,null=True)
    price=models.PositiveIntegerField(default=1000)
    options=(
        ("4G","4G"),
        ("5G","5G"),
        ("3G","3G")
    )
    bands=models.CharField(max_length=150,choices=options,default="5G")
    doptions=(
        ("LED","LED"),
        ("AMLED","AMLED"),
        ("SMLED","SMLED"),
    )
    display=models.CharField(max_length=50,choices=doptions,default="LED")
    

    def __str__(self):
        return self.name