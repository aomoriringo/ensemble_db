from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

from .models import *

def index(request):
    latest_work_list = Work.objects.order_by('-title')[:5]
    context = RequestContext(request, {
        'latest_work_list': latest_work_list,
    })
    return render(request, 'index.html', context)

def detail(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    return render(request, 'work/detail.html', {'work': work})

def results(request, work_id):
    response = "You're looking at the results of work %s."
    return HttpResponse(response % work_id)

