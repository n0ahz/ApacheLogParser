from django.conf.urls import url
from .views import apachelogs_list_page,apachelogs_uploads,logparser

urlpatterns = [
    url(r'^upload/$', apachelogs_uploads , name='apachelog_upload'),
    url(r'^list/$', apachelogs_list_page, name='apachelog_list'),
    url(r'^parse/$', logparser , name='apachelog_parse'),
]
