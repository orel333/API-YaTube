from django.shortcuts import get_object_or_404
from rest_framework import exceptions
from rest_framework import filters
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Follow, Group, Post, User
from .serializers import CommentSerializer
from .serializers import FollowSerializer
from .serializers import GroupSerializer
from .serializers import logger
from .serializers import PostSerializer


class CreateListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass

class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    

    def perform_create(self, serializer):
        """Переопределение метода создания комментария.
        Предусмотрено автоматическое присвоение автора."""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """Переопределение методов изменения поста.
        Предусмотрена проверка авторства."""
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'У вас недостаточно прав для выполнения данного действия.'
            )
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        """Переопределение метода удаления поста.
        Предусмотрена проверка авторства."""
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'У вас недостаточно прав для выполнения данного действия.'
            )
        super().perform_destroy(instance)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для комментариев."""
    serializer_class = CommentSerializer

    def perform_update(self, serializer):
        """Переопределение методов изменения комментария.
        Предусмотрена проверка авторства."""
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'У вас недостаточно прав для выполнения данного действия.'
            )
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        """Переопределение метода удаления комментария.
        Предусмотрена проверка авторства."""
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'У вас недостаточно прав для выполнения данного действия.'
            )
        super().perform_destroy(instance)

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
    """Вьюсет для групп."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(CreateListViewSet):
    """Вьюсет для подписок."""
    logger.debug('viewset starts')
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
        logger.debug(f'вьюсет: {self.request.data}')
        following_user = get_object_or_404(
            User, username=self.request.data.get('following')
        )
        follow_dict = {
            'user': self.request.user,
            'following': following_user
        }
        serializer.save(**follow_dict)
