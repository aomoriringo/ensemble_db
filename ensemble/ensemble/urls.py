from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^work/(?P<work_id>[0-9]+)/$', views.detail, name='detail'),
        url(r'^work/(?P<work_id>[0-9]+)/results/$', views.results, name='results'),
]