import json
from django.db import IntegrityError
from django.shortcuts import render
from .models import ApacheLog
from sites.models import Site
from log_formats.models import LogFormats
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import apache_log_parser


def create(request):
    site_obj = Site.objects.order_by("-id")
    site_list = list(site_obj)
    return render(request, 'upload_log.html', {'sites': site_list})


def parse_log(request):
    site_obj = Site.objects.order_by("-id")
    site_list = list(site_obj)
    log_format_id = int(request.POST.get('log_format_id'))
    site_id = int(request.POST.get('site_id'))
    log_format_model = LogFormats.objects.get(id=log_format_id)
    log_format = str(log_format_model.log_format)
    line_parser = apache_log_parser.make_parser(log_format)

    uploaded_file = request.FILES.get('uploaded_file')

    parsed_log_list = []
    log_lines = []
    for line in uploaded_file.file:
        try:
            line = line.strip()
            if bool(line) and line not in log_lines:
                data = line_parser(line)
                apl = ApacheLog(**data)
                apl.full_line = line
                apl.site_id = site_id
                apl.log_format_id = log_format_id
                parsed_log_list.append(apl)
                log_lines.append(line)
        except Exception as e:
            return render(request, 'upload_log.html', {'msg': "Invalid file or Log format!", 'site_id': site_id, 'sites': site_list})

    try:
        from itertools import islice
        start = 0
        batch_size = 10
        stop = batch_size
        while stop <= len(parsed_log_list):
            batch = list(islice(parsed_log_list, start, stop))
            if not batch:
                break
            ApacheLog.objects.bulk_create(batch, batch_size)
            start = stop
            stop += batch_size
            if stop > len(parsed_log_list):
                stop = len(parsed_log_list)
    except IntegrityError as ie:
        # should not happen as duplicates should be removed before..
        print "Duplicates found!"
        # return render(request, 'upload_log.html', {'msg': "Uniqueness failed! Most probably file uploaded before!", 'site_id': site_id, 'sites': site_list})
    except Exception, e:
        return render(request, 'upload_log.html', {'msg': e.message, 'site_id': site_id, 'sites': site_list})
    return HttpResponseRedirect('/log/log_list')


def log_list(request):
    last_obj = ApacheLog.objects.order_by('-id').first()
    if not last_obj:
        return render(request, 'log_list.html', {})

    # logs = list(ApacheLog.objects.filter(format_id=last_id).order_by('id')[:30])

    # pagination
    paginator = Paginator(ApacheLog.objects.order_by('-time_second'), 30)  # Show 30 logs per page
    page = request.GET.get('page')
    try:
        logs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        logs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        logs = paginator.page(paginator.num_pages)
    site_name = Site.objects.filter()[0].site_name
    return render(request, 'log_list.html', {'logs': logs, 'siteName': site_name})


def load_log_format(request):
    site_id = request.GET.get('site_id')
    log_list = LogFormats.objects.filter(site_id=site_id)
    return HttpResponse(json.dumps(list(log_list.values())), content_type="application/json")

