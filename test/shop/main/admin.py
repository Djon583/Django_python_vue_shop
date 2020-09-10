from django.contrib import admin
from main.models import Room, Chat, Products, Category, ListOrders, Comments


"""======================  Chat ======================="""
class RoomAdmin(admin.ModelAdmin):
    """Комнаты чата"""
    list_display = ("creater", "invited_user", "date")

    def invited_user(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])


class ChatAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("room", "user", "text", "date")

admin.site.register(Chat, ChatAdmin)
admin.site.register(Room, RoomAdmin)


"""======================  Show product ======================="""
class CategoryAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("id", "name")

class ProductsAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("category_id","id", "name", "price", "details","link_img")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(ListOrders)
admin.site.register(Comments)