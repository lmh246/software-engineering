from django.db import models
from django.utils.six import python_2_unicode_compatible

# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class LunBo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos',blank=True,null=True)

# Create your models here.
