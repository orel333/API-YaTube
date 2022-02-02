from rest_framework import filters, mixins, viewsets

from .permissions import OwnerOrReadOnly


class CreateListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """Миксин для обработки запросов POST и GET(list)."""
    pass


class BaseViewSet(viewsets.ModelViewSet):
    """Базовый вьюсет с установкой пермишена Автор-или-Чтение.
    Также заложена сортировка."""
    permission_classes = (OwnerOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)
