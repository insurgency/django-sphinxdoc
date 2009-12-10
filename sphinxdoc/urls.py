# encoding: utf-8

from django.conf.urls.defaults import *
from django.views.generic import list_detail

from sphinxdoc import models

app_info = {
    'queryset': models.App.objects.all().order_by('name'),
    'template_object_name': 'app',
}


urlpatterns = patterns('',
    url(
        r'^$',
        list_detail.object_list,
        app_info,
    ),
    url(
        r'^(?P<slug>[-\w]+)/$',
        'foo',
        name='app-index',
    ),
    # url(
    #     r'^(?P<lang>[a-z-]+)/$',
    #     djangodocs.views.language,
    # ),
    # url(
    #     r'^(?P<lang>[a-z-]+)/(?P<version>[\w.-]+)/$',
    #     djangodocs.views.document,
    #     {'url': ''},
    #     name = 'document-index',
    # ),
    # url(
    #     r'^(?P<lang>[a-z-]+)/(?P<version>[\w.-]+)/search/$',
    #     djangodocs.views.search,
    #     name = 'document-search',
    # ),
    # url(
    #     r'^(?P<lang>[a-z-]+)/(?P<version>[\w.-]+)/_objects/$',
    #     djangodocs.views.objects_inventory,
    #     name = 'objects-inv',
    # ),
    # url(
    #     r'^(?P<lang>[a-z-]+)/(?P<version>[\w.-]+)/_images/(?P<path>.*)$',
    #     djangodocs.views.images,
    # ),
    # url(
    #     r'^(?P<lang>[a-z-]+)/(?P<version>[\w.-]+)/_source/(?P<path>.*)$',
    #     djangodocs.views.source,
    # ),
    # url(
    #     r'^(?P<lang>[a-z-]+)/(?P<version>[\w.-]+)/(?P<url>[\w./-]*)/$',
    #     djangodocs.views.document,
    #     name = 'document-detail',
    # ),
)
