# надо проверить автор ли, если нет - только почитать можно
from rest_framework import permissions

from .serializers import logger


class OwnerOrReadOnly(permissions.BasePermission):
    logger.debug('Инициировано определение прав пользователя на запрос')

    def has_permission(self, request, view):
        logger.debug('Определение пермишена на уровне запроса')
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        logger.debug('Определение пермишена на уровне объекта')
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
