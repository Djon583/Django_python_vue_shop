from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import Room, Chat, Products, Category, ListOrders, Comments

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=6, max_length=100,
            write_only=True)

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')



"""======================Product======================="""
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","name")        

class ProductsSerializer(serializers.ModelSerializer):
    link_img = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Products
        fields = ("category_id","id","name","price","details","link_img")        

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("status","product_id","user_id","text")        

"""===========================Chat==================================="""
class UsersSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")

class RoomSerializers(serializers.ModelSerializer):
    """Сериализация комнат чата"""
    creater = UsersSerializer()
    invited = UsersSerializer(many=True)
    class Meta:
        model = Room
        fields = ("id", "creater", "invited", "date")

class ChatSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    user = UsersSerializer()
    class Meta:
        model = Chat
        fields = ("user", "text", "date")

class ChatPostSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    class Meta:
        model = Chat
        fields = ("room", "text")
