from email.mime import base
from posixpath import basename
from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet
from .views import FollowViewSet
from .views import GroupViewSet
from .views import PostViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router_v1.register(r'follow', FollowViewSet, basename='follow')
router_v1.register(r'groups', GroupViewSet, basename='group')
router_v1.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
