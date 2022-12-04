from socket import fromshare
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from django import forms
class OperationsForm(forms.Form):
    num1=forms.IntegerField(required=True)
    num2=forms.IntegerField(required=True)

    def clean(self):
        cleaned_data=super().clean()    #/ cleaned_data("num1":100,"num2":300)
        n1=cleaned_data.get("num1")
        n2=cleaned_data.get("num2")
        if n1 <1:
            msg="invalid value for number1"
            self.add_error("num1",msg)
        
        if n2 <1:
            msg="invalid value for n2"
            self.add_error("num2",msg)
        


class AddView(View):
    def get(self,request,*args,**kwargs):
        form=OperationsForm()
        return render(request,"add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=OperationsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,"add.html")
        else:
            return render(request,"add.html",{"form":form})


        # n1=request.POST["num1"]
        # n2=request.POST["num2"]
        # res=int(n1)+int(n2)
        # return render(request,"add.html",{"result":res})

class SubstractionView(View):
    def get(self,request,*args,**kwargs):
        form=OperationsForm()
        return render(request,"sub.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=OperationsForm(request.POST)
        if form.is_valid():
            print(form.changed_data)
            return render(request,"sub.html")
        else:
            return render(request,"sub.html",{"form":form})

        # n1=request.POST["num1"]
        # n2=request.POST["num2"]
        # res=int(n1)-int(n2)
        # return render(request,"sub.html",{"result":res})
class ExponentView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"exp.html")
    def post(self,request,*args,**kwargs):
        n=int(request.POST["num"])
        res=n**3
        return render(request,"exp.html",{"result":res})
class MultiplicationView(View):
    def get(self,request,*args,**kwargs):
        form=OperationsForm
        return render(request,"mul.html",{"form":form})
    def post(self,request,*args, **kwargs):
        n1=request.POST["num1"]
        n2=request.POST["num2"]
        res=int(n1)*int(n2)
        # print("result",res)
        return render(request,"mul.html",{"result":res})
        # numcheckview,primenumberview,factorialview
class NumcheckView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"numcheck.html")
    def post(self,request,*args,**kwargs):
        n=int(request.POST["num"])
        if n%2==0:
            print("EVEN")
        else:
            print("ODD")
        return render(request,"numcheck.html")
class PrimeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"prime.html")
    def post(self,request,*args,**kwargs):
        n=int(request.POST["num"])
        for i in range(2,n):
            if n%i==0:
                print("NOT PRIME")
                break
            else:
                print("PRIME")
        return render(request,"prime.html")        

class FactorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"fact.html")
    def post(self,request,*args,**kwargs):
        n=int(request.POST["num"])
        f=1
        for i in range(1,n+1):
            f=f*i
        print(f)
        return render(request,"fact.html")

class WordForm(forms.Form):
    n1=forms.CharField(label="masterword",required=True)
    n2=forms.CharField(label="checkword",required=True)

class CheckView(View):
    def get(self,request,*args, **kwargs):
        form=WordForm()
        return render(request,"word.html",{"form":form})
    def post(self,request,*args, **kwargs):
        form=WordForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("n1")
            n2=form.cleaned_data.get("n2")
            f=0
        for i in n2:
            if n2.count(i)>n1.count(i):
                f=1
        if f==1:
            res="flase"
        else:
            res="true"
        return render(request,"word.html",{"result":res,"form":form})










