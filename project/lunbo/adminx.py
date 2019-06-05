import xadmin
from .models import LunBo

# Register your models here.
class LunAdmin(object):
    list_display = ['name', 'description', 'owner', 'image', 'created_time']
    search_fields = ['name', 'description', 'owner', 'image', 'created_time']
    list_filter = ['name', 'description', 'owner', 'image', 'created_time']

xadmin.site.register(LunBo,LunAdmin)