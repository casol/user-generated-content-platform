from django.contrib import admin

from .models import Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'custom_url',
                    'content', 'created', 'active']
    list_filter = ['created', 'active']
