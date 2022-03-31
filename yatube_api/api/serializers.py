import logging
import sys
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User

formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(message)s - строка %(lineno)s'
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
handler.setFormatter(formatter)
logger.disabled = False
logger.debug('Логирование запущено')


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор публикаций."""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    text = serializers.CharField(default='')

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        read_only_fields = ('id', 'image', 'pub_date')

    def validate_text(self, value):
        """Валидация текста публикации.
        Проверяется, чтобы поле не было пустым."""
        logger.debug('Сериализатор: начата валидация текста; value:'
                     f'{value}, value.strip():{value.strip()}')
        if value is None or value.strip() == '':
            logger.debug('Текстовое поле определено пустым')
            raise serializers.ValidationError(
                'Обязательное поле.'
            )
        return value


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор комментариев."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created', 'post')
        read_only_fields = ('id', 'post', 'created')

    def validate_text(self, value):
        """Валидация текста комментария.
        Проверяется, чтобы поле не было пустым."""
        logger.debug('Начата валидация текста')
        if value is None or value.strip() == '':
            logger.debug('Текстовое поле определено пустым')
            raise serializers.ValidationError(
                'Обязательное поле.'
            )
        return value

    def create(self, validated_data):
        """Переопределение функции создания текста.
        Оценивается присутствие поля 'text' в теле запроса."""
        if 'text' not in self.initial_data:
            raise serializers.ValidationError(
                'Обязательное поле.'
            )
        comment = Comment.objects.create(**validated_data)
        return comment


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор сообществ."""

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор подписок."""
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]
        fields = ('user', 'following')
        model = Follow

    def validate_following(self, value):
        """Валидация подписки.
        Проверяется, чтобы пользователь не подписывается сам на себя."""
        following = get_object_or_404(User, username=value)
        user = self.context['request'].user
        if following == user:
            raise serializers.ValidationError(
                'Подписываться на себя непозволительно.'
            )
        return value
