from django.contrib import admin

from .models import Comment, Follow, Group, Post
from yatube_api.settings import EMPTY_VALUE


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'pub_date',
        'text',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = EMPTY_VALUE

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'slug',
        'title',
        'description',
    )
    search_fields = ('title', 'slug')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'text',
        'created'
    )
    search_fields = ('text', 'author')
    list_filter = ('created',)
    empty_value_display = EMPTY_VALUE

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'following',
    )
    search_fields = ('user', 'following')
    list_filter = ('user', 'following')
    empty_value_display = EMPTY_VALUE

