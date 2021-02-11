from django.contrib import admin
from .models import Post, Category, Comment, MyImage


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content')
    list_filter = ('category', 'author')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'content')
    list_filter = ('post', 'author')


admin.site.register(MyImage)
admin.site.register(Category)
admin.site.site_header = "Blog Admin"
