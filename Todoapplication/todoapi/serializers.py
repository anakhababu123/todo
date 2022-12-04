from rest_framework import serializers
from myapp.models import Todos

class TodosSerializer(serializers.Serializer):
    task_name=serializers.CharField()
    username=serializers.CharField()


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todos
        fields=["name","description","category","price","image"]


class ReviewSerializers(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)

    class Meta:
        model=Reviews
        fields=["comment","user","product","rating"]

    def create(self,validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Reviews.objects.create(**validated_data,user=user,product=product)

class CartSerializers(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    class Meta:
        model=Carts
        fields=["product","user","date"]
    def create(self,validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Carts.objects.create(user=user,product=product,**validated_data)




