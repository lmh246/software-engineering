from django.db import models
from django.contrib.auth.models import AbstractUser # 拓展用户模型

from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
# Create your models here.

# 用户表
class User(AbstractUser):
    user_name = models.CharField(max_length=100) # 用户名
    user_password = models.CharField(max_length=100) # 密码

# 类别
class CategoryTable(models.Model):
    category_name = models.CharField(max_length=100) # 类别名字

# 论坛
class ForumTable(models.Model):
    forum_name = models.CharField(max_length=100) # 论坛名字


# 文章表
@python_2_unicode_compatible
class ArticleTable(models.Model):
    article_title = models.CharField(max_length=70) # 文章标题
    article_text = models.TextField() # 文章内容
    created_time = models.DateField() # 文章创建时间
    modified_time = models.DateField() # 文章修改时间
    avg_grade = models.IntegerField(default=0) # 文章平均评分
    comment_count = models.IntegerField(default=0)
    article_user = models.ForeignKey(User) # 对应的用户
    article_category = models.ForeignKey(CategoryTable) # 对应的类别
    article_forum = models.ForeignKey(ForumTable) # 对应论坛名
    # 浏览量
    views = models.PositiveIntegerField(default=0)
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])



    def __str__(self):
        return self.article_title




# 拓展用户模型
# class User(AbstractUser):
#     nick_name = models.CharField(max_length=50,blank=True)  # 用户昵称
#     personal_des = models.TextField() # 用户说明


