from ..models import ArticleTable,CategoryTable
from django import template

# 进行注册为模板标签
register = template.Library()

# 获取指定书目的文章
@register.simple_tag
def get_recent_article(nums=5):
    return ArticleTable.objects.all().order_by('-created_time')[:nums]


# 归档模板
@register.simple_tag
def archives():
    return ArticleTable.objects.dates('created_time','month',order='DESC')


# 分类模板
@register.simple_tag
def get_categories():
    return CategoryTable.objects.all()