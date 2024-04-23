
from rest_framework import serializers
from .models import Playlist, Channel

class PlaylistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class ChannelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'