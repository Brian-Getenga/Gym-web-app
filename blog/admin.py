""" from django.contrib import admin
from .models import BlogPost, Category, Tag, Bookmark, Like

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'status')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Bookmark)
admin.site.register(Like)
 """

from django.contrib import admin
from .models import BlogPost, Category, Tag

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'status')
    list_filter = ('status', 'category', 'tags')
    search_fields = ('title', 'content', 'excerpt')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
