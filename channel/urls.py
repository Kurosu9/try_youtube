from rest_framework import routers
from django.urls import path

from .views import ChannelModelViewSet, PlaylistModelViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path("channel/", ChannelModelViewSet.as_view({'get': 'list', 'post': 'create'}), name="channel"),
    path("channel/<int:pk>/", ChannelModelViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="channel"),

    path("playlist/", PlaylistModelViewSet.as_view({'get': 'list', 'post': 'create'}), name="channel"),
    path("playlist/<int:pk>/", PlaylistModelViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="channel"),

]

urlpatterns += router.urls