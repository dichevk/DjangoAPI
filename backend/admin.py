from django.contrib import admin
from models.Contact.contact_model import Contact
from models.Item.item_model import Order, Item

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'email')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'item')