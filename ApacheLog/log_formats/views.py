from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import LogFormats
from .forms import LogFormatForm
from django.db.models import Q
from sites.models import Site
# Create your views here.


def logformat_add_page(request):
    form = LogFormatForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/logformats/list/")
    context = {
        "form": form,
        "title": "Add Log Format",
    }
    return render(request, 'log_formats/log_format_add.html', context)


def logformat_list_page(request):
    log_list = LogFormats.objects.order_by("-id")

    # for search
    query = request.GET.get('q')
    if query:
        log_list = log_list.filter(Q(site__site_name__startswith=query))

    context = {
        "log_list": log_list,
        "title": "List of Logformat",
    }
    return render(request, 'log_formats/log_format_list.html', context)


def logformat_edit_page(request, id=None):
    detail = get_object_or_404(LogFormats, id=id)
    form = LogFormatForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/logformats/list/")
    context = {
        "form": form,
        "title": "Edit Log Format",
    }
    return render(request, 'log_formats/log_format_add.html', context)


def logformat_delete_page(request, id=None):
    detail = get_object_or_404(LogFormats, id=id)
    detail.delete()
    return HttpResponseRedirect("/logformats/list/")
