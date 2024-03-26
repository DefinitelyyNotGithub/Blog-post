from django.contrib import admin
from .models import (
    Post,
    Category,
    UserComments,

)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'visibility', 'category']
    list_filter = ['visibility', 'category', 'autor', 'spread_date']

@admin.register(UserComments)
class UserCommentAdmin(admin.ModelAdmin):
    list_filter = ['created_date']
    list_display = ['autor', 'created_date', 'post']

admin.site.register(Category)