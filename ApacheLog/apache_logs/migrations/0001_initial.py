# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-10-26 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0001_initial'),
        ('log_formats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApacheLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remote_host', models.GenericIPAddressField(null=True)),
                ('remote_logname', models.TextField(null=True)),
                ('remote_user', models.TextField(null=True)),
                ('request_first_line', models.TextField(null=True)),
                ('request_header_referer', models.TextField(null=True)),
                ('request_header_user_agent', models.TextField(null=True)),
                ('request_header_user_agent_browser_family', models.TextField(null=True)),
                ('request_header_user_agent_browser_version_string', models.CharField(max_length=10, null=True)),
                ('request_header_user_agent_is_mobile', models.NullBooleanField()),
                ('request_header_user_agent_os_family', models.CharField(max_length=25, null=True)),
                ('request_header_user_agent_os_version_string', models.CharField(max_length=10, null=True)),
                ('request_http_ver', models.CharField(max_length=10, null=True)),
                ('request_method', models.CharField(choices=[('GET', 'Get'), ('POST', 'POST'), ('PUT', 'Put'), ('DELETE', 'Delete'), ('HEAD', 'Head'), ('CONNECT', 'Connect'), ('OPTIONS', 'Options'), ('TRACE', 'Trace'), ('PATCH', 'Patch')], max_length=10, null=True)),
                ('request_url', models.TextField()),
                ('request_url_fragment', models.TextField(null=True)),
                ('request_url_hostname', models.TextField(null=True)),
                ('request_url_netloc', models.TextField(null=True)),
                ('request_url_password', models.TextField(null=True)),
                ('request_url_path', models.TextField(null=True)),
                ('request_url_port', models.IntegerField(null=True)),
                ('request_url_query', models.TextField(null=True)),
                ('request_url_query_dict', models.TextField(null=True)),
                ('request_url_query_list', models.TextField(null=True)),
                ('request_url_query_simple_dict', models.TextField(null=True)),
                ('request_url_scheme', models.TextField(null=True)),
                ('request_url_username', models.TextField(null=True)),
                ('response_bytes', models.DecimalField(decimal_places=6, max_digits=60, null=True)),
                ('status', models.IntegerField(null=True)),
                ('time_received', models.TextField(null=True)),
                ('time_received_datetimeobj', models.DateTimeField(null=True)),
                ('time_received_isoformat', models.TextField(null=True)),
                ('time_received_tz_datetimeobj', models.DateTimeField(null=True)),
                ('time_received_tz_isoformat', models.TextField(null=True)),
                ('time_received_utc_datetimeobj', models.DateTimeField(null=True)),
                ('time_received_utc_isoformat', models.TextField(null=True)),
                ('time_second', models.DecimalField(decimal_places=6, max_digits=60, null=True)),
                ('time_millisecond', models.DecimalField(decimal_places=6, max_digits=60, null=True)),
                ('log_format', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='log_formats.LogFormats')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='apachelog',
            unique_together=set([('site', 'log_format', 'remote_host', 'request_url', 'time_received_utc_isoformat')]),
        ),
    ]
