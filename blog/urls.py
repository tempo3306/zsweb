# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/2/2 14:34
'''
from django.conf.urls import url
from . import views
urlpatterns = [
    # post views
    #url(r'^$', views.post_list, name='post_list'),
url(r'^$', views.PostListView.as_view(),name='post_list'),
url(r'^(?P<post_id>\d+)/share/$', views.post_share,
    name='post_share'),  #邮件共享
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]