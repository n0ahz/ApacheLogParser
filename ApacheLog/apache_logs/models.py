from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from sites.models import Site

class ApacheLog(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    receive_dateTime = models.DateTimeField()
    http_method = models.CharField(max_length=10)
    http_response = models.CharField(max_length=10)
    response_time = models.TimeField()
    url = models.CharField(max_length=300)

