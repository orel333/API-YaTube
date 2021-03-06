from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .mixins import BaseViewSet, CreateListViewSet
from .serializers import CommentSerializer
from .serializers import FollowSerializer
from .serializers import GroupSerializer
from .serializers import logger
from .serializers import PostSerializer
from posts.models import Comment, Follow, Group, Post, User


class PostViewSet(BaseViewSet):
    """Вьюсет для постов."""
    logger.debug('Вьюсет для постов запустился')
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    ordering_fields = ('pub_date',)

    def perform_create(self, serializer):
        """Переопределение метода создания комментария.
        Предусмотрено автоматическое присвоение автора."""
        logger.debug('Вьюсет для постов: perform create')
        logger.debug(serializer.__dict__)
        serializer.save(author=self.request.user)


class CommentViewSet(BaseViewSet):
    """Вьюсет для комментариев."""
    serializer_class = CommentSerializer
    ordering_fields = ('created',)

    def get_queryset(self):
        """Переопределение метода получения queryset.
        Предусмотрено получение комментариев к определенному посту."""
        post_id = self.kwargs.get('post_id')
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        """Переопределение метода создания комментария.
        Предусмотрено автоматическое присвоение автора и поста."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        comment_dict = {
            'author': self.request.user,
            'post': post
        }
        serializer.save(**comment_dict)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для сообществ."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(CreateListViewSet):
    """Вьюсет для подписок."""
    logger.debug('Запущен вьюсет подписок')
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """Переопределение метода получения queryset.
        Предусмотрено получение подписок определенного пользователя."""
        new_queryset = Follow.objects.filter(user=self.request.user)
        return new_queryset

    def perform_create(self, serializer):
        """Переопределение метода создания подписки.
        Предусмотрено автоматическое присвоение владельца подписки."""
        logger.debug('Начато создание подписки, '
                     f'self.request.data: {self.request.data}')
        following_user = get_object_or_404(
            User, username=self.request.data.get('following')
        )
        follow_dict = {
            'user': self.request.user,
            'following': following_user
        }
        serializer.save(**follow_dict)
