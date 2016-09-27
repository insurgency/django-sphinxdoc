"""
URL conf for django-sphinxdoc.

"""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^$',
        views.OverviewList.as_view(),
        name='docs-list',
    ),
    url(
        r'^(?P<slug>[\w-]+)/search/$',
        views.ProjectSearchView(),
        name='doc-search',
    ),
    # These URLs have to be without the / at the end so that relative links in
    # static HTML files work correctly and that browsers know how to name files
    # for download
    url(
        (r'^(?P<slug>[\w-]+)/(?P<type_>_images|_static|_downloads|_source)/'
         r'(?P<path>.+)$'),
        views.sphinx_serve,
    ),
    url(
        r'^(?P<slug>[\w-]+)/_objects/$',
        views.objects_inventory,
        name='objects-inv',
    ),
    url(
        r'^(?P<slug>[\w-]+)/$',
        views.documentation,
        {'path': ''},
        name='doc-index',
    ),
    url(
        r'^(?P<slug>[\w-]+)/genindex/$',
        views.documentation,
        {'path': 'genindex'},
        name='doc-genindex',
    ),
    url(
        r'^(?P<slug>[\w-]+)/(?P<path>.+)/$',
        views.documentation,
        name='doc-detail',
    ),
]
