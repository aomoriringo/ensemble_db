from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^work/(?P<work_id>[0-9]+)/$', views.work_detail, name='work_detail'),
        url(r'^writer/(?P<writer_id>[0-9]+)/$', views.writer_detail, name='writer_detail'),
        url(r'^instrument/(?P<instrument_id>[0-9]+)/$', views.instrument_detail, name='instrument_detail'),
        url(r'^music_category/(?P<music_category_id>[0-9]+)/$', views.music_category_detail, name='music_category_detail'),
        url(r'^publisher/(?P<publisher_id>[0-9]+)/$', views.publisher_detail, name='publisher_detail'),
        url(r'^work/(?P<work_id>[0-9]+)/results/$', views.results, name='results'),
]
