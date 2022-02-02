from django.contrib.auth import get_user_model
from django.db import models

from yatube_api.settings import TRUNCATE_NUM

User = get_user_model()


class Group(models.Model):
    """Модель сообществ."""
    title = models.CharField('Название сообщества', max_length=200)
    description = models.TextField('Описание сообщества')
    slug = models.SlugField('Индекс URL', unique=True)

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель публикаций."""
    text = models.TextField('Текст поста', null=True, blank=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации')
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        default=None,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа поста'
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

    def __str__(self):
        return self.text[:TRUNCATE_NUM]


class Comment(models.Model):
    """Модель комментариев."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Публикация комментария'
    )
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.text[:TRUNCATE_NUM]

    class Meta:
        ordering = ('created',)
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'


class Follow(models.Model):
    """Модель подписок."""
    user = models.ForeignKey(
        User,
        verbose_name='Подписчик',
        on_delete=models.CASCADE,
        related_name='follows_of_user')

    following = models.ForeignKey(
        User,
        verbose_name='Подписка на автора',
        on_delete=models.CASCADE,
        related_name='follows_for_author'
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        constraints = (
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='not_for_self'
            ),
            models.UniqueConstraint(
                fields=('user', 'following'), name='unique_follow'
            ),
        )
