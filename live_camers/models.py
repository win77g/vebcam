from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None,db_index=True, unique=True)
# вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class LiveCameras(models.Model):
    country = models.ForeignKey(Country,blank=True, null=True, default=None,on_delete=models.CASCADE,to_field='name')
    city = models.CharField(max_length=120,blank=True, null=True, default=None)
    name = models.CharField(max_length=120,blank=True, null=True, default=None)
    url = models.CharField(max_length=120,blank=True, null=True, default=None)
    slug = models.SlugField(blank=True, null=True, default=None)
    top = models.BooleanField(default=False)


     # вывод одного поля
    def __str__(self):
        return " %s" % self.city
    class Meta:
        verbose_name = 'Камера'
        verbose_name_plural = 'Камеры'



