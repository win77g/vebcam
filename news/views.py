from django.shortcuts import render

from .models import *
from rest_framework import viewsets,permissions
from news.serializers import *


# сериаизация заголовка
class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_fields = ('id',)

class NewsFromCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_fields = ('category',)
# сериаизация заголовка
class CategoryNewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CategoryNews.objects.all()
    serializer_class = CategoryNewsSerializer

