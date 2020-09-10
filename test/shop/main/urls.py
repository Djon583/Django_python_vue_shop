# coding=utf-8
from django.urls import path
from main.views import *
from django.conf.urls import url
from . import views

urlpatterns = [
    path('room/', Rooms.as_view()),
    path('dialog/', Dialog.as_view()),
    path('users/', AddUsersRoom.as_view()),
    path('category/', CategoryViews.as_view()),
    path('products/', ProductsViews.as_view()),
    url('reg/', views.UserCreate.as_view(), name='account-create'),
]