from .models import Baner
from rest_framework import serializers


class BanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baner
        fields = ('image','slug')
