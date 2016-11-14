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
    local_ip = models.CharField(max_length=20, null=True)
    format_id =  models.IntegerField()
    site_id = models.IntegerField()
    status = models.IntegerField()
    response_bytes_clf = models.CharField(max_length=30,null=True)
    remote_host = models.CharField(max_length=50,null=True)
    request_method = models.CharField(max_length=4,null=True)
    request_url_path = models.CharField(max_length=500,null=True)
    time_received_tz_isoformat = models.CharField(max_length=50,null=True)

    class Meta:
        unique_together = ('site_id','local_ip','status','time_received_tz_isoformat','request_url_path','response_bytes_clf','request_method')



