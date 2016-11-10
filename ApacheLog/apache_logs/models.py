from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from sites.models import Site

class ApacheLog(models.Model):
    #site = models.ForeignKey(Site, on_delete=models.CASCADE)

    # receive_dateTime = models.DateTimeField()
    # http_method = models.CharField(max_length=10)
    # http_response = models.CharField(max_length=10)
    # response_time = models.TimeField()
    # url = models.CharField(max_length=300)

    site_id =  models.IntegerField()
    status = models.IntegerField()

    request_first_line =models.CharField(max_length=500,null=True)
    response_bytes_clf = models.CharField(max_length=30,null=True)
    remote_host = models.CharField(max_length=500,null=True)
    request_http_ver  = models.CharField(max_length=500,null=True)
    request_url_port  = models.CharField(max_length=5,null=True)
    remote_logname = models.CharField(max_length=30,null=True)
    request_method = models.CharField(max_length=4,null=True)
    time_received = models.CharField(max_length=30,null=True)


