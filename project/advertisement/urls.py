from django.conf.urls import url
from . import views

app_name = 'lunbo'
urlpatterns = [
    url(r'^upload_adv/',views.upload_adv,name='upload_adv'),
]