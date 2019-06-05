from django.db import models
from django.utils.six import python_2_unicode_compatible

# Create your models here.
# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100) # 名字
    email = models.EmailField(max_length=255) # 邮箱
    url = models.URLField(blank=True) # 个人网站
    text = models.TextField() # 用户发表的内容
    created_time = models.DateTimeField(auto_now_add=True) # 记录评论的时间
    score = models.IntegerField(default=0) # 评分
    post = models.ForeignKey('website.ArticleTable')

    def __str__(self):
        return self.text[:20]