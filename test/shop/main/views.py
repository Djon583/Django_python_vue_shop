from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth.models import User

from main.serializers import UserSerializer
from rest_framework.authtoken.models import Token

from main.models import Room, Chat, Products, Category, ListOrders, Comments
from main.serializers import (RoomSerializers, ChatSerializers, ChatPostSerializers,  UsersSerializer)
from main.serializers import ProductsSerializer, CategorySerializer, CommentsSerializer


"""======================Product View======================="""
class CategoryViews(APIView):
    """List Products"""
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response({"data": serializer.data})

class ProductsViews(APIView):
    permission_classes = [permissions.AllowAny, ]
    def get(self,request):
        #category = request.GET.get("category")
        #products = Products.objects.filter(category_id=category)
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response({"data": serializer.data})

"""======================Comments============================"""
class CommentsViews(APIView):
    permission_classes = [permissions.AllowAny, ]
    def get(self,request):
        product = request.GET.get("product")
        products = Products.objects.filter(product_id=product)
        #products = Products.objects.all()
        serializer = CommentsSerializer(products, many=True)
        return Response({"data": serializer.data})

"""======================Chat======================="""
class Rooms(APIView):
    """Комнаты чата"""
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        rooms = Room.objects.filter(Q(creater=request.user) | Q(invited=request.user))
        serializer = RoomSerializers(rooms, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        Room.objects.create(creater=request.user)
        return Response(status=201)


class Dialog(APIView):
    """Диалог чата, сообщение"""
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        room = request.GET.get("room")
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        # room = request.data.get("room")
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)

class AddUsersRoom(APIView):
    """Добавление юзеров в комнату чата"""
    def get(self, request):
        users = User.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        room = request.data.get("room")
        user = request.data.get("user")
        try:
            room = Room.objects.get(id=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)

"""=======================CreateUser================"""
class UserCreate(APIView):
    """ 
    Creates the user. 
    """
    permission_classes = [permissions.AllowAny, ]
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
