from rest_framework import routers
from django.urls import path
from .views import VideoModelViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path("videos/", VideoModelViewSet.as_view({'get': 'list', 'post': 'create'}), name="video"),
    path("videos/<int:pk>/", VideoModelViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="video")
]

urlpatterns += router.urls
