from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Playlist, Channel
from .serializers import PlaylistSerializers, ChannelSerializers

class PlaylistModelViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializers

class ChannelModelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializers
