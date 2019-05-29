from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.bible_list, name='bible_list'),
    re_path(r'(?P<pk>\d+)/$', views.bible_detail, name='bible_detail'),
]
