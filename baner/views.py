from django.shortcuts import render

from .models import *
from rest_framework import viewsets
from baner.serializers import *
# Create your views here.

# сериаизация заголовка
class BanerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = [permissions.AllowAny, ]
    queryset = Baner.objects.all()
    serializer_class = BanerSerializer
# Create your views here.
