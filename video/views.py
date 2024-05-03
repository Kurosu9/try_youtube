from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializers

class VideoModelViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

