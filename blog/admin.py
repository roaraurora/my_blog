from django.contrib import admin

# Register your models here.
from .models import Tag, Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'modified_name', 'category', 'author')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
