# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-28 08:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apache_logs', '0002_auto_20181028_1351'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='apachelog',
            unique_together=set([]),
        ),
    ]
