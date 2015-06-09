from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

from .models import *
from parameter import AMAZON_TRACKING_ID

def index(request):
    def get_category_dic(category):
        children = MusicCategory.objects.filter(parent=category).order_by('order', 'number')
        if children.exists():
            l = [get_category_dic(c) for c in children]
            count = sum([c['count'] for c in l])
        else:
            l = []
            count = WorkMusicCategory.objects.filter(music_category=category).count()
        return {"object": category, "children": l, "count": count}

    latest_work_list = Work.objects.order_by('-id')[:30]
    latest_writer_list = Writer.objects.order_by('-id')[:10]
    root_category_list = MusicCategory.objects.filter(parent=None).order_by('order', 'number')
    category_list = [get_category_dic(c) for c in root_category_list]
    context = RequestContext(request, {
        'latest_work_list': latest_work_list,
        'latest_writer_list': latest_writer_list,
        'category_list': category_list,
    })
    return render(request, 'index.html', context)

def work_detail(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    players = {}
    for player in work.player_set.all():
        instruments = {}
        for i in player.playerinstrument_set.all():
          id = i.id
          name = i.override_description or i.instrument.short_name or i.instrument.name
          if i.number > 1:
              name = str(i.number) + " " + name
          instruments[id] = {'name': name,
                             'link_id': i.instrument.id}
        players[player.order] = instruments
    context = RequestContext(request, {
        'work': work,
        'players': players,
        'amazon_id': AMAZON_TRACKING_ID,
    })
    return render(request, 'work/detail.html', context)

def instrument_detail(request, instrument_id):
    instrument = get_object_or_404(Instrument, pk=instrument_id)
    context = RequestContext(request, {
        'instrument': instrument
    })
    return render(request, 'instrument/detail.html', context)

def music_category_detail(request, music_category_id):
    music_category = get_object_or_404(MusicCategory, pk=music_category_id)
    context = RequestContext(request, {
        'music_category': music_category
    })
    return render(request, 'music_category/detail.html', context)

def publisher_detail(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    published_works = [x for x in publisher.work_set.all()]
    context = RequestContext(request, {
        'publisher': publisher,
        'published_works': published_works
    })
    return render(request, 'publisher/detail.html', context)

def writer_detail(request, writer_id):
    writer = get_object_or_404(Writer, pk=writer_id)
    compose_works = [x.work for x in writer.workcomposer_set.all()]
    arrange_works = [x.work for x in writer.workarranger_set.all()]
    context = RequestContext(request, {
        'writer': writer,
        'compose_works': compose_works,
        'arrange_works': arrange_works,
    })
    return render(request, 'writer/detail.html', context)

def results(request, work_id):
    response = "You're looking at the results of work %s."
    return HttpResponse(response % work_id)

