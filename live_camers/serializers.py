from .models import LiveCameras,Country
from rest_framework import serializers


class LiveCamerasSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveCameras
        fields = ('country','city','name','url','slug','top')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)
