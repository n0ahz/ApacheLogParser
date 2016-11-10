from django.conf.urls import url
from .views import create,parseLog


urlpatterns = [
    url(r'^uploadlog/$', create, name='uploadlog'),
    url(r'^parse/$', parseLog, name='parse'),

]
