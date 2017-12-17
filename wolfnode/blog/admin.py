from django.contrib import admin
from .models import Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    readonly_fields = ['id']


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)