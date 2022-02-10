# надо проверить автор ли, если нет - только почитать можно
from rest_framework import permissions

from yatube_api.settings import BLACK_LIST_ACCESS

from .methods import to_dict
from .serializers import logger


class OwnerOrReadOnly(permissions.BasePermission):
    """Пермишен Автор-или-Чтение.
    Без регистрации пользователи могут делать только безопасные запросы.
    С регистрацией пользователи могут делать POST-запросы либо
    запросы на изменение, если являются авторами объекта."""
    logger.debug('Инициировано определение прав пользователя на запрос')

    def has_permission(self, request, view):
        logger.debug('Определение пермишена на уровне запроса')
        BL = False
        try:
            jti = request._auth.get('jti')
            to_read = open('access_blacklist.txt', 'r')
            str = to_read.read()
            dict = to_dict(str)
            logger.debug(dict)
            logger.debug(jti)
            if jti in dict.values():
                BL = True
                logger.debug('This token was blacklisted')
        except:
            pass
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated and not BL)
        )

    def has_object_permission(self, request, view, obj):
        BL = False
        try:
            jti = request._auth.get('jti')
            logger.debug(BLACK_LIST_ACCESS)
            logger.debug(jti)
            if jti in BLACK_LIST_ACCESS.values():
                BL = True
                logger.debug('This token was blacklisted')
        except:
            pass
        logger.debug('Определение пермишена на уровне объекта')
        logger.debug(dir(request))
        return (
            request.method in permissions.SAFE_METHODS
            or (obj.author == request.user and not BL)
        )
