from rest_framework import routers
from django.urls import path

from .views import UserModelViewSet, NotificationModelViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path("user", UserModelViewSet.as_view({'get': 'list', 'post': 'create'}), name="user"),
    path("<int:pk>/", UserModelViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="user"),

    path("notification/", NotificationModelViewSet.as_view({'get': 'list', 'post': 'create'}), name="user"),
    path("notification/<int:pk>/", NotificationModelViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="user"),

]

urlpatterns += router.urls