from rest_framework import viewsets
from .models import User, Notification
from .serializers import UserSerializers, NotificationSerializers

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
class NotificationModelViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

