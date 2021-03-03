from django.contrib import admin

from .models import Content

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'content', 'created']
    list_filter = ['created']
