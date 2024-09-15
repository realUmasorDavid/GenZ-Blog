from django.contrib import admin
from .models import *

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['id', 'title', 'content']
    readonly_fields = ['created_at']
    list_filter = ['created_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'commentFromBlog', 'commentDetail', 'created_at']
    search_fields = ['id', 'commentDetail']
    readonly_fields = ['created_at']
    list_filter = ['created_at']

class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'like', 'created_at']
    search_fields = ['id', 'blog', 'like']
    readonly_fields = ['created_at']
    list_filter = ['created_at']

class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'created_at']
    search_fields = ['id', 'email']
    readonly_fields = ['created_at']

class TestCommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'created_at']
    search_fields = ['comment', 'created_at']
    readonly_fields = ['created_at']

admin.site.register(TestComment, TestCommentAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(NewsLetter, NewsLetterAdmin)