from django.contrib import admin
from .models import *

class LiveCamerasAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   list_display = ['country','city','name','url','slug','top']

class Meta:
    model = LiveCameras
# Register your models here.
admin.site.register(LiveCameras,LiveCamerasAdmin)
# Register your models here.

class CountryAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   list_display = ['name']

class Meta:
    model = Country
# Register your models here.
admin.site.register(Country,CountryAdmin)
# Register your models here.
