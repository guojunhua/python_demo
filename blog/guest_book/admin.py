from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'active', 'posted')
    list_filter = ('active', 'posted')
    search_fields = ('name', 'message')
    ordering = ('-posted',)


admin.site.register(Message, MessageAdmin)
