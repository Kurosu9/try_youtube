from rest_framework import serializers
from .models import Channel, Playlist

class ChannelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

class PlaylistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'