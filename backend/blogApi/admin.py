from django.contrib import admin
from .models import Post, Category, Comment


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content')
    list_filter = ('category', )


admin.site.register(Comment)
admin.site.register(Category)
admin.site.site_header = "Blog Admin"
