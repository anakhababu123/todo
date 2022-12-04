from django.shortcuts import render,redirect

# Create your views here.
from myapp.forms import TodoForm,TodoModelForm,RegistrationForm,LoginForm

from django.views.generic import View,ListView,DetailView,CreateView,UpdateView
from myapp.models import todos,Todos
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

def signin_required(fn):
    def wrapper(request,*args,**kw):
        if not request.user.is_authenticated:
            messages.error(request,"u must login to perform this action")
            return redirect("signin")
        else:
            return fn(request,*args,**kw)
    return wrapper
@method_decorator(signin_required,name="dispatch")        
class TodoCreateView(CreateView):
    model=Todos
    form_class=TodoModelForm
    template_name: str="add-todo.html"
    success_url=reverse_lazy("todo-list")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"todo hasbeen created")
        return super().form_valid(form)





    # def get(self,request,*args,**kwargs):
    #     form=TodoModelForm()
    #     return render(request,"add-todo.html",{"form":form})
    # def post(self,request,*args, **kwargs):
    #     form=TodoModelForm(request.POST)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         messages.success(request,"todo has been created")
    #         # t_name=form.cleaned_data.get("task_name")
    #         # usr=form.cleaned_data.get("user")
    #         # Todos.objects.create(task_name=t_name,user=usr)
    #         return redirect("todo-list")


            # last_todo_id=todos[-1].get("id")
            # id=last_todo_id+1
            # form.cleaned_data["id"]=id
            # todos.append(form.cleaned_data)
            # print(todos)


            # print(form.cleaned_data)
            # todos.append(form.cleaned_data)


            # t_name=(form.cleaned_data.get("task_name"))
            # usr=(form.cleaned_data.get("user"))
            # new_todo={"id":7,"task_name":t_name,"user":usr}
            # todos.append(new_todo)
            # print(todos)
        #     return render(request,"add-todo.html")
        # else:
        #     messages.error(request,"todo not created")
        #     return render(request,"add-todo.html",{"form":form})
@method_decorator(signin_required,name="dispatch")        
class TodoListView(ListView):
    model=Todos
    context_object_name="todos"
    template_name="todo-list.html"

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)


    # def get(self,request,*args, **kwargs):
    #     qs=Todos.objects.filter(user=request.user)
    #     # all_todos=todos
    #     return render(request,"todo-list.html",{"todos":qs})

    

class TodoDetailView(DetailView):
    model=Todos
    template_name: str="todo-detail.html"
    context_object_name=str="todo"
    pk_url_kwarg: str="id"



    # def get(self,request,*args, **kwargs):
    #     id=kwargs.get("id")
    #     qs=Todos.objects.get(id=id)
    #     # id=kwargs.get("id")
    #     # todo=[todo for todo in todos if todo.get("id")==id]
    #     return render(request,"todo-detail.html",{"todo":qs})
@method_decorator(signin_required,name="dispatch")        
class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Todos.objects.filter(id=id).delete()
        # todo=[todo for todo in todos if todo.get("id")==id].pop()
        # todos.remove(todo)
        return redirect("todo-list")
@method_decorator(signin_required,name="dispatch")        
class TodoEditView(UpdateView):
    model=Todos
    form_class=TodoModelForm
    template_name: str="todo-update.html"
    pk_url_kwarg: str="id"
    success_url=reverse_lazy("todo-list")

    def form_valid(self, form):
        messages.success(self.request,"todo change")
        return super().form_valid(form)
    




    # def get(self,request,*args, **kwargs):
    #     id=kwargs.get("id")
    #     todo=Todos.objects.get(id=id)
    #     # todo=Todos.objects.filter(id=id).values()[0]
    #     # todo=[todo for todo in todos if todo.get("id")==id].pop()
    #     form=TodoModelForm(instance=todo)
    #     return render(request,"todo-update.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     todo=Todos.objects.get(id=id)

        # form=TodoModelForm(request.POST,instance=todo)
        # if form.is_valid():
        #     form.save()
        #     messages.success(request,"todo updated successfully")
            # data=form.cleaned_data
            # id=kwargs.get("id")
            # Todos.objects.filter(id=id).update(**form.cleaned_data)
            # todo=[todo for todo in todos if todo.get("id")==id].pop()
            # todo.update(data)
        #     return redirect("todo-list")
        # else:
        #     messages.error(request,"todo not updated")
        #     return render(request,"todo-update.html",{"form":form})


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
                return redirect("todo-list")
            else:
                messages.error(request,"invalid")
                return render(request,"login.html",{"form":form})
@signin_required
def signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")



