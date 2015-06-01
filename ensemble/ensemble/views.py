from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

from .models import *
from parameter import AMAZON_TRACKING_ID

def index(request):
    latest_work_list = Work.objects.order_by('-id')[:10]
    latest_writer_list = Writer.objects.order_by('-id')[:10]
    context = RequestContext(request, {
        'latest_work_list': latest_work_list,
        'latest_writer_list': latest_writer_list,
    })
    return render(request, 'index.html', context)

def work_detail(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    context = RequestContext(request, {
        'work': work,
        'amazon_id': AMAZON_TRACKING_ID,
    })
    return render(request, 'work/detail.html', context)

def writer_detail(request, writer_id):
    writer = get_object_or_404(Writer, pk=writer_id)
    return render(request, 'writer/detail.html', {'writer': writer})

def results(request, work_id):
    response = "You're looking at the results of work %s."
    return HttpResponse(response % work_id)

