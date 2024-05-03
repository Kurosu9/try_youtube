from rest_framework import viewsets
from .models import Shorts
from .serializers import ShortsSerializers

class ShortsModelViewSet(viewsets.ModelViewSet):
    queryset = Shorts.objects.all()
    serializer_class = ShortsSerializers

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

