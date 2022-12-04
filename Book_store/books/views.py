# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

# Create your views here.

#books=[ 
# "id":1,"name":name1,"author":atname,"price",290
# ]
from django.views.generic import View,ListView,DetailView
from books.forms import BookForm,BookModelForm,RegistrationForm,LoginForm
from books.models import books,Books
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



class BookCreateView(View):
    def get(self,request,*args,**kwargs):
        form=BookModelForm()
        return render(request,"add-book.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"book has been created")

            # b_name=form.cleaned_data.get("name")
            # b_author=form.cleaned_data.get("author")
            # b_price=form.cleaned_data.get("price")
            # Books.objects.create(name=b_name,author=b_author,price=b_price)
            return redirect("book-list")
            # print(form.cleaned_data)
            # books.append(form.cleaned_data)
            # return render(request,"add-book.html")
        else:
            messages.error(request,"book is not created")
            return render(request,"add-book.html",{"form":form})


class BookListView(ListView):
    model=Books
    context_object_name="books"
    template_name="book-list.html"


    
    # def get(self,request,*args,**kwargs):
    #     bs=Books.objects.all()
    #     return render(request,"book-list.html",{"books":bs})
    #     # all_books=books
    #     # return render(request,"book-list.html",{"books":all_books})



class BookDetailView(DetailView):

    model=Books
    context_object_name="book"
    template_name="book-detail.html"
    pk_url_kwarg: str="id"


    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     bs=Books.objects.get(id=id)

        # return render(request,"book-detail.html",{"book":bs})
        # book=[book for book in books if book.get("id")==id].pop()
        # return render(request,"book-detail.html",{"book":book})

class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Books.objects.filter(id=id).delete()
        # book=[book for book in books if book.get("id")==id].pop()
        # books.remove(book)
        return redirect("book-list")

class BookEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        # book=[book for book in books if book.get("id")==id].pop()
        # bk=Books.objects.filter(id=id).values()[0]
        form=BookModelForm(instance=book)
        return render(request,"book-update.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        form=BookModelForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            messages.success(request,"todo updated successfully")

            # data=form.cleaned_data
            # id=kwargs.get("id")
            # Books.objects.filter(id=id).update(**form.cleaned_data)
            # book=[book for book in books if book.get("id")==id].pop()
            # book.update(data)
            return redirect("book-list")
        else:
            messages.error(request,"todo not updated")
            return render(request,"todo-update.html",{"form":form})

class RegistraionView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form}) 
    def post(self,request,*args, **kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"registraion completed successfully")
            return redirect("signin")
        else:
            messages.error(request,"registration failed")
            return render(request,"registration.html",{"form":form})


class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return redirect("book-list")
            else:
                messages.error(request,"invalid")
                return render(request,"login.html",{"form":form})

def signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")



        

