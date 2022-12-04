from django.db import models
from django.contrib.auth.models import User

# Create your models here.
books=[
    {"id":1,"name":"Manju","author":"M.T.Vasudevan Nair","price":120},
    {"id":2,"name":"You Only Live Once","author":"Stuti Changle","price":163},
    {"id":3,"name":"The Kid Who Came From Space","author":"Ross Welford","price":215},
    {"id":4,"name":"Balyakalasakhi","author":"Vaikom Muhammad Basheer","price":110},
]

class Books(models.Model):
    name=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()


    def _str_(self):
        return self.name
