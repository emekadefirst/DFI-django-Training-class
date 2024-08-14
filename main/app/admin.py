from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_field = ['id', 'title', 'content']
    readonly_field = ['created_at']
    list_filter = ['created_at']
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'created_at']
    search_field = ['id', 'comment']
    readonly_field = ['created_at']
    list_filter = ['created_at']
    
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'like','created_at']
    search_field = ['id', 'blog', 'like',]
    readonly_field = ['created_at']
    list_filter = ['created_at']
    
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'created_at']
    search_field = ['email']
    readonly_field = ['created_at']
    list_filter = ['created_at']
    
class TestCommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'created_at']
    search_fields = ['comment', 'created_at']
    readonly_field = ['created_at']
    list_filter = ['created_at']
    
    
admin.site.register(TestComment, TestCommentAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(NewsLetter, NewsLetterAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
