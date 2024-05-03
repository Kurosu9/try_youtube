from rest_framework import viewsets
from .models import Channel, Playlist
from .serializers import ChannelSerializers, PlaylistSerializers

class ChannelModelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializers

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
class PlaylistModelViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializers

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

