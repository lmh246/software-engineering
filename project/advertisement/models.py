from django.db import models
from django.utils.six import python_2_unicode_compatible

# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class AdverTise(models.Model):
    name = models.CharField(max_length=100)  # 公司名称
    created_time = models.DateTimeField(auto_now_add=True) # 添加时间
    capital = models.IntegerField(max_length=100) # 资金
    duration = models.IntegerField(max_length=100)# 投放时间
    image = models.ImageField(upload_to='photos',blank=True,null=True) # 宣传图片

# Create your models here.
