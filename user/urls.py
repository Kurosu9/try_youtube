from rest_framework import routers
from django.urls import path

from .views import UserModelViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path("", UserModelViewSet.as_view({'get': 'list', 'post': 'create'}), name="user"),
    path("<int:pk>/", UserModelViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="user")
]

urlpatterns += router.urls