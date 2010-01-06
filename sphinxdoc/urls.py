# encoding: utf-8

from django.conf.urls.defaults import *
from django.views.generic import list_detail

from sphinxdoc import models

app_info = {
    'queryset': models.App.objects.all().order_by('name'),
    'template_object_name': 'app',
}


urlpatterns = patterns('sphinxdoc.views',
    url(
        r'^$',
        list_detail.object_list,
        app_info,
    ),
    url(
        r'^(?P<slug>[\w-]+)/search/$',
        'search',
        name='doc-search',
    ),
    url(
        r'^(?P<slug>[\w-]+)/_images/(?P<path>.*)$',
        'images',
    ),
    url(
        r'^(?P<slug>[\w-]+)/_source/(?P<path>.*)$',
        'source',
    ),
    url(
        r'^(?P<slug>[\w-]+)/_objects/$',
        'objects_inventory',
        name='objects-inv',
    ),
    url(
        r'^(?P<slug>[\w-]+)/$',
        'documentation',
        {'url': ''},
        name='doc-index',
    ),
    url(
        r'^(?P<slug>[\w-]+)/(?P<url>(([\w-]+)/)+)$',
        'documentation',
        name='doc-detail',
    ),
)
