from django.conf.urls import url
from .views import create,parseLog,log_list


urlpatterns = [
    url(r'^uploadlog/$', create, name='uploadlog'),
    url(r'^parse/$', parseLog, name='parse'),
    url(r'^loglist/$',log_list,name='loglist')

]
