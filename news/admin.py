from django.contrib import admin
from .models import *

class NewsAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку

   list_display = ['name','category','author','image_img','date','hot_news']
   readonly_fields = ['image_img',]


class Meta:
    model = News
# Register your models here.
admin.site.register(News,NewsAdmin)

class CategoryNewsAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   list_display = ['name']

class Meta:
    model = CategoryNews
# Register your models here.
admin.site.register(CategoryNews,CategoryNewsAdmin)
# Register your models here.
