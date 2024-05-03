from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializers

class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

