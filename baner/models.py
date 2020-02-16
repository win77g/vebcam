from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
def image_folder(instance,filename):
    filename = instance.slug +'.'+filename.split('.')[1]
    return "{0}/{1}".format(instance.slug,filename)
# Create your models here.
class Baner(models.Model):

    image = models.ImageField(upload_to=image_folder, blank=True, null=True, default=None)
    slug = models.SlugField(blank=True, null=True, default=None)

# вывод одного поля
    def __str__(self):
        return " %s" % self.slug
    class Meta:
        verbose_name = 'Банер'
        verbose_name_plural = 'Банер'

    def image_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True
