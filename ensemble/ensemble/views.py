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
    players = {}
    for player in work.player_set.all():
        instruments = {}
        for i in player.playerinstrument_set.all():
          id = i.instrument.id
          name = i.override_description or i.instrument.short_name or i.instrument.name
          if i.number > 1:
              name = str(i.number) + " " + name
          instruments[id] = name
        players[player.order] = instruments
    context = RequestContext(request, {
        'work': work,
        'players': players,
        'amazon_id': AMAZON_TRACKING_ID,
    })
    return render(request, 'work/detail.html', context)

def instrument_detail(request, instrument_id):
    instrument = get_object_or_404(Instrument, pk=instrument_id)
    return render(request, 'instrument/detail.html')

def writer_detail(request, writer_id):
    writer = get_object_or_404(Writer, pk=writer_id)
    return render(request, 'writer/detail.html', {'writer': writer})

def results(request, work_id):
    response = "You're looking at the results of work %s."
    return HttpResponse(response % work_id)

