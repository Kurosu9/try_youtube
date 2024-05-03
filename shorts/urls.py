from rest_framework import routers
from django.urls import path
from .views import ShortsModelViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path("shorts/", ShortsModelViewSet.as_view({'get': 'list', 'post': 'create'}), name="shorts"),
    path("shorts/<int:pk>/", ShortsModelViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="shorts")
]

urlpatterns += router.urls
