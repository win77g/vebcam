from django.contrib import admin
from .models import *

class BanerAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   #    list_display = [field.name for field in Product._meta.fields]
   #    inlines = [ProductImageInline]
   list_display = ['image_img']
   readonly_fields = ['image_img',]
   # fields = ['category', 'title', 'slug', 'metakey', 'metadesc', 'text_redactor', 'text_redactor_full', 'tag', 'timestamp', 'autor', 'image', 'image_img', 'body', 'likes', 'dislikes']

class Meta:
    model = Baner
# Register your models here.
admin.site.register(Baner,BanerAdmin)
# Register your models here.
