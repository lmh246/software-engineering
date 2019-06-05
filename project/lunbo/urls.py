from django.conf.urls import url
from . import views

app_name = 'lunbo'
urlpatterns = [
    url(r'^upload/',views.upload_image,name='upload_img'),
]