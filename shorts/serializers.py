from rest_framework import serializers
from .models import Shorts

class ShortsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shorts
        fields = '__all__'