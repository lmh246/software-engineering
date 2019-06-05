from django.contrib import admin
import xadmin
from .models import Comment

# Register your models here.
class CommnetAdmin(object):
    list_display = ['name', 'email', 'url', 'text', 'created_time', 'post']
    search_fields = ['name', 'email', 'url', 'text', 'created_time', 'post']
    list_filter = ['name', 'email', 'url', 'text', 'created_time', 'post']

xadmin.site.register(Comment,CommnetAdmin)