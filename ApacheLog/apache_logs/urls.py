from django.conf.urls import url

from .views import create,parseLog,log_list

from .views import create,parseLog,loadLogFormat



urlpatterns = [
    url(r'^uploadlog/$', create, name='uploadlog'),
    url(r'^parse/$', parseLog, name='parse'),
    url(r'^loglist/$',log_list,name='loglist'),
    url(r'^loadlogformat/$', loadLogFormat, name='loadLogFormat'),

]
