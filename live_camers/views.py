from django.shortcuts import render

from .models import *
from rest_framework import viewsets,permissions
from live_camers.serializers import *


# сериаизация заголовка
class LiveCamersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LiveCameras.objects.all()
    serializer_class = LiveCamerasSerializer
    filter_fields = ('top',)

class LiveCamersCountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LiveCameras.objects.all()
    serializer_class = LiveCamerasSerializer
    filter_fields = ('country',)

class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

