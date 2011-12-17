# encoding: utf-8
"""
Views for django-shinxdoc.

"""
import datetime
import json
import os.path

from django.core import urlresolvers
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from django.views.static import serve
from haystack.views import SearchView

from sphinxdoc.forms import ProjectSearchForm
from sphinxdoc.models import Project, Document


BUILDDIR = os.path.join('_build', 'json')
CACHE_MINUTES = 5


@cache_page(60 * CACHE_MINUTES)
def documentation(request, slug, path):
    """
    Displays the contents of a :class:`sphinxdoc.models.Document`.

    ``slug`` specifies the project, the document belongs to, ``path`` is the
    path to the original JSON file relative to the builddir and without the
    file extension. ``path`` may also be a directory, so this view checks if
    ``path/index`` exists, before trying to load ``path`` directly.

    """
    project = get_object_or_404(Project, slug=slug)
    path = path.rstrip('/')

    try:
        index = 'index' if path == '' else '%s/index' % path
        doc = Document.objects.get(project=project, path=index)
    except ObjectDoesNotExist:
        doc = get_object_or_404(Document, project=project, path=path)

    # genindex and modindex get a special template
    templates = (
        'sphinxdoc/%s.html' % os.path.basename(path),
        'sphinxdoc/documentation.html',
    )

    data = {
        'project': project,
        'doc': json.loads(doc.content),
        'env': json.load(open(
                os.path.join(project.path, BUILDDIR,
                'globalcontext.json'), 'rb')),
        'update_date':  datetime.datetime.fromtimestamp(
                os.path.getmtime(os.path.join(project.path, BUILDDIR,
                'last_build'))),
        'search': urlresolvers.reverse('doc-search', kwargs={'slug': slug}),
    }

    return render_to_response(templates, data,
            context_instance=RequestContext(request))


@cache_page(60 * CACHE_MINUTES)
def objects_inventory(request, slug):
    """
    Renders the ``objects.inv`` as plain text.

    """
    project = get_object_or_404(Project, slug=slug)
    response = serve(
        request,
        document_root=os.path.join(project.path, BUILDDIR),
        path='objects.inv',
    )
    response['Content-Type'] = 'text/plain'
    return response


@cache_page(60 * CACHE_MINUTES)
def sphinx_serve(request, slug, type_, path):
    """
    Serves sphinx static and other files.

    """
    project = get_object_or_404(Project, slug=slug)
    return serve(
        request,
        document_root=os.path.join(project.path, BUILDDIR, type_),
        path=path,
    )


class ProjectSearchView(SearchView):
    """
    Inherits :class:`SearchView` and handles a search request and displays the
    results as a simple list.

    """
    def __init__(self):
        SearchView.__init__(self, form_class=ProjectSearchForm,
                template='sphinxdoc/search.html')

    def __call__(self, request, slug):
        self.slug = slug
        return SearchView.__call__(self, request)

    def build_form(self):
        """
        Instantiates the form that should be used to process the search query.

        """
        return self.form_class(self.request.GET, slug=self.slug,
                searchqueryset=self.searchqueryset, load_all=self.load_all)

    def extra_context(self):
        return {
            'project': Project.objects.get(slug=self.slug),
        }
