from django.conf.urls import url
from . import views

app_name = 'website'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/',views.register,name='register'),  # http://localhost:8000/register/
    url(r'^article/([0-9]+)/', views.detail, name='detail'), # 每篇文章的详情页
    url(r'^about/',views.about,name='about'),# 关于页面
    url(r'^contact/',views.contact,name='contact'),# 联系页面
    url(r'^person/',views.person,name='person'),# 联系页面
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
]