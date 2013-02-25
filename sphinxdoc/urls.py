# encoding: utf-8
"""
URL conf for django-sphinxdoc.

"""
from django.conf.urls.defaults import patterns, url

from sphinxdoc.views import ProjectSearchView
from sphinxdoc.views import OverviewList


urlpatterns = patterns('sphinxdoc.views',
    url(
        r'^$',
        OverviewList.as_view(),
    ),
    url(
        r'^(?P<slug>[\w-]+)/search/$',
        ProjectSearchView(),
        name='doc-search',
    ),
    # These URLs have to be without the / at the end so that relative links in
    # static HTML files work correctly and that browsers know how to name files
    # for download
    url(
        r'^(?P<slug>[\w-]+)/(?P<type_>_images|_static|_downloads|_source)/' + \
                r'(?P<path>.+)$',
        'sphinx_serve',
    ),
    url(
        r'^(?P<slug>[\w-]+)/_objects/$',
        'objects_inventory',
        name='objects-inv',
    ),
    url(
        r'^(?P<slug>[\w-]+)/$',
        'documentation',
        {'path': ''},
        name='doc-index',
    ),
    url(
        r'^(?P<slug>[\w-]+)/(?P<path>.+)/$',
        'documentation',
        name='doc-detail',
    ),
)
