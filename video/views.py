from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializers
from rest_framework.response import Response
from rest_framework import status


class VideoModelViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def list_playlist_videos(self, request, playlist=None):
        try:
            videos = self.queryset.filter(playlist=playlist)
            serializer = self.serializer_class(videos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Video.DoesNotExist:
            return Response({"message": "Playlist does not exist"}, status=status.HTTP_404_NOT_FOUND)

