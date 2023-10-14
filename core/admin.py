from django.contrib import admin
from .models import Newsletter, Client, Message

# Register your models here

class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ["id"]

class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "id"]

admin.site.register(Newsletter)
admin.site.register(Client, ClientAdmin)
admin.site.register(Message, MessageAdmin)
