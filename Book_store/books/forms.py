# from re import T
# from unicodedata import name
from dataclasses import fields
from django import forms
from books.models import Books
from django.contrib.auth.models import User


class BookForm(forms.Form):
    id=forms.IntegerField(label="id",required=True)
    name=forms.CharField(label="name",required=True)
    author=forms.CharField(label="author",required=True)
    price=forms.IntegerField(label="price",required=True)



class BookModelForm(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"})
        }
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))