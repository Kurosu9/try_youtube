from rest_framework import routers
from django.urls import path
from .views import CommentModelViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path("comments/", CommentModelViewSet.as_view({'get': 'list', 'post': 'create'}), name="comment"),
    path("comments/<int:pk>/", CommentModelViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="comment")
]

urlpatterns += router.urls
