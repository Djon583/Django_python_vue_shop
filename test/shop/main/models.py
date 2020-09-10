from django.db import models

from django.contrib.auth.models import User
# from djoser.urls.base import User


"""======================  Chat ======================="""
class Room(models.Model):
    """Модель комнаты чата"""
    creater = models.ForeignKey(User, verbose_name="Создатель", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="Участники", related_name="invited_user")
    date = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Комната чата"
        verbose_name_plural = "Комнаты чатов"

class Chat(models.Model):
    """Модель чата"""
    room = models.ForeignKey(Room, verbose_name="Комната чата", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=500)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение чата"
        verbose_name_plural = "Сообщения чатов"

"""==========================Product=============================="""

class Category(models.Model):
    """Модель категория"""
    name = models.CharField(max_length=100, null=False, default='', verbose_name="Название")
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категорий"
    def __str__(self):
        return self.name

class Products(models.Model):
    """Модель Продукт"""
    category_id = models.ForeignKey(Category, related_name='category', verbose_name="Категория", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, default='', verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    details = models.CharField(max_length=100, null=False, default='', verbose_name="Характеристика")
    link_img = models.ImageField(blank=False, null=True, verbose_name="Картинки")
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    def __str__(self):
        return self.name

""" ========= ListOrders =============================== """
class ListOrders(models.Model):
    user_id = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, verbose_name="Пользователь ID")
    product_id = models.ForeignKey(Products, related_name='product_order', on_delete=models.CASCADE, verbose_name="Продукт ID")
    class Meta:
        verbose_name = 'Список заказов'
        verbose_name_plural = 'Список заказов'
    def __str__(self):
        return 'Список заказов'

""" ========= Comments =============================== """
class Comments(models.Model):
    status = models.IntegerField(default='0', verbose_name="Статус");
    product_id = models.ForeignKey(Products, related_name='product', on_delete=models.CASCADE, verbose_name="Продукт ID")
    user_id = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE, verbose_name="Пользователь ID")
    text = models.CharField(max_length=200, null=False, default='', verbose_name="Комментария")
    class Meta:
        verbose_name = 'Комментария'
        verbose_name_plural = 'Коментария'
    def __str__(self):
        return 'Комментария'
