from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from myapp.models import Todos
from todoapi.serializers import TodosSerializer


class TodosView(ViewSet):
    # def list(self,request,*args, **kwargs):
    #     qs=Todos.objects.all()
    #     serializer=TodosSerializer(qs,many=True)
    #     return Response(data=serializer.data)
    
    # def create(self,request,*args, **kwargs):
    #     serializer=TodosSerializer(data=request.data)
    #     if serializer.is_valid():
    #         Todos.objects.create(**serializer.validated_data)
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.error)

    
    # def retrieve(self,request,*args, **kwargs):
    #     id=kwargs.get("pk")
    #     qs=Todos.objects.get(id=id)
    #     serializer=TodosSerializer(qs)
    #     return Response(data=serializer.data)

    
    # def update(self,request,*args, **kwargs):
    #     return Response(data="updating resourses")
    
    # def destroy(self,request,*args, **kwargs):
    #     id=kwargs.get("pk")
    #     Todos.objects.get(id=id).delete()
    #     return Response(data="deleted")