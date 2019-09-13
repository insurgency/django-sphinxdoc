"""URL conf for django-sphinxdoc."""

from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r'^$', views.OverviewList.as_view(), name='docs-list'),
    re_path(r'^(?P<slug>[\w-]+)/search/$', views.ProjectSearchView(), name='doc-search'),
    # These URLs have to be without the / at the end so that relative links in
    # static HTML files work correctly and that browsers know how to name files
    # for download
    re_path(r'^(?P<slug>[\w-]+)/(?P<type_>_images|_static|_downloads|_source)/(?P<path>.+)$', views.sphinx_serve),
    re_path(r'^(?P<slug>[\w-]+)/_objects/$', views.objects_inventory, name='objects-inv'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.documentation, {'path': ''}, name='doc-index'),
    re_path(r'^(?P<slug>[\w-]+)/genindex/$', views.documentation, {'path': 'genindex'}, name='doc-genindex'),
    re_path(r'^(?P<slug>[\w-]+)/(?P<path>.+)/$', views.documentation, name='doc-detail'),
]
