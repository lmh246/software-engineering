import xadmin
from .models import AdverTise

# Register your models here.
class AdvertiseAdmin(object):
    list_display = ['name', 'capital', 'duration', 'image', 'created_time']
    search_fields = ['name', 'capital', 'duration', 'image', 'created_time']
    list_filter = ['name', 'capital', 'duration', 'image', 'created_time']

xadmin.site.register(AdverTise,AdvertiseAdmin)