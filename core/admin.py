from django.contrib import admin
from .models import QR

@admin.register(QR)
class CustomModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'type', 'content', 'author', 'color1', 'color2',
        'createdAt', 'dotStyle', 'eyeStyle', 'isPublic', 'logoImage', 'verified'
    )
    search_fields = ('id', 'name', 'author', 'type')