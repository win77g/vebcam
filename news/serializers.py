from .models import *
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','name','category','image','slug','description','description_short','author','date','hot_news')

class CategoryNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryNews
        fields = ('name',)


