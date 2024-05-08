from rest_framework import routers
from django.urls import path
from .views import VideoModelViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path("video/videos/", VideoModelViewSet.as_view({'get': 'list', 'post': 'create'}), name="video"),
    path("playlist/<int:playlist>/videos", VideoModelViewSet.as_view({'get': 'list_playlist_videos'}), name="playlist_videos"),
    path("video/videos/<int:pk>/", VideoModelViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="video")
]

urlpatterns += router.urls
