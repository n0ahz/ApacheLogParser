from __future__ import unicode_literals

from django.db import models
from sites.models import Site


class LogFormats(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    log_format = models.CharField(max_length=100)

    def __unicode__(self):
        return self.sites
