from rest_framework import routers

from .views import PlaylistModelViewSet, ChannelModelViewSet

router = routers.DefaultRouter()
router.register(
    "playlist", viewset=PlaylistModelViewSet, basename="playlist"
)

router.register(
    "channel", viewset=ChannelModelViewSet, basename="channel"
)

urlpatterns = [

]

urlpatterns += router.urls