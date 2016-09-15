"""
Views for django-shinxdoc.

"""
import datetime
import json
import os.path

from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.core import urlresolvers
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from django.views.generic import ListView
from django.views.static import serve
from haystack.views import SearchView

from sphinxdoc.decorators import user_allowed_for_project
from sphinxdoc.forms import ProjectSearchForm
from sphinxdoc.models import Project, Document


BUILDDIR = os.path.join('_build', 'json')
CACHE_MINUTES = getattr(settings, 'SPHINXDOC_CACHE_MINUTES', 5)


@user_allowed_for_project
@cache_page(60 * CACHE_MINUTES)
def documentation(request, slug, path):
    """Displays the contents of a :class:`sphinxdoc.models.Document`.

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

    try:
        env = json.load(open(os.path.join(project.path, BUILDDIR,
                                          'globalcontext.json'), 'r'))
    except IOError:
        # It is possible that file does not exist anymore (for example, because
        # make clean to prepare for running make again), we do not want to
        # display an error to the user in this case
        env = None

    try:
        update_date = datetime.datetime.fromtimestamp(os.path.getmtime(
            os.path.join(project.path, BUILDDIR, 'last_build')))
    except OSError:
        # It is possible that file does not exist anymore (for example, because
        # make clean to prepare for running make again), we do not want to
        # display an error to the user in this case
        update_date = datetime.datetime.fromtimestamp(0)

    data = {
        'base_template': getattr(settings, 'SPHINXDOC_BASE_TEMPLATE', 'base.html'),
        'project': project,
        'doc': json.loads(doc.content),
        'env': env,
        'update_date': update_date,
        'search': urlresolvers.reverse('doc-search', kwargs={'slug': slug}),
    }

    return render_to_response(templates, data,
                              context_instance=RequestContext(request))


@user_allowed_for_project
@cache_page(60 * CACHE_MINUTES)
def objects_inventory(request, slug):
    """Renders the ``objects.inv`` as plain text."""
    project = get_object_or_404(Project, slug=slug)
    response = serve(
        request,
        document_root=os.path.join(project.path, BUILDDIR),
        path='objects.inv',
    )
    response['Content-Type'] = 'text/plain'
    return response


@user_allowed_for_project
@cache_page(60 * CACHE_MINUTES)
def sphinx_serve(request, slug, type_, path):
    """Serves sphinx static and other files."""
    project = get_object_or_404(Project, slug=slug)
    return serve(
        request,
        document_root=os.path.join(project.path, BUILDDIR, type_),
        path=path,
    )


class ProjectSearchView(SearchView):
    """Inherits :class:`~haystack.views.SearchView` and handles a search
    request and displays the results as a simple list.

    """
    def __init__(self):
        SearchView.__init__(self, form_class=ProjectSearchForm,
                            template='sphinxdoc/search.html')

    def __call__(self, request, slug):
        self.slug = slug
        try:
            return SearchView.__call__(self, request)
        except PermissionDenied:
            if request.user.is_authenticated():
                raise
            path = request.build_absolute_uri()
            return redirect_to_login(path)

    def build_form(self):
        """Instantiates the form that should be used to process the search
        query.

        """
        return self.form_class(self.request.GET, slug=self.slug,
                               searchqueryset=self.searchqueryset,
                               load_all=self.load_all)

    def extra_context(self):
        """Adds the *project*, the contents of ``globalcontext.json`` (*env*)
        and the *update_date* as extra context.

        """
        project = Project.objects.get(slug=self.slug)
        if not project.is_allowed(self.request.user):
            raise PermissionDenied

        try:
            env = json.load(open(os.path.join(project.path, BUILDDIR,
                                              'globalcontext.json'), 'r'))
        except IOError:
            # It is possible that file does not exist anymore (for example,
            # because make clean to prepare for running make again), we do not
            # want to display an error to the user in this case
            env = None

        try:
            update_date = datetime.datetime.fromtimestamp(os.path.getmtime(
                os.path.join(project.path, BUILDDIR, 'last_build')))
        except OSError:
            # It is possible that file does not exist anymore (for example,
            # because make clean to prepare for running make again), we do not
            # want to display an error to the user in this case
            update_date = datetime.datetime.fromtimestamp(0)

        return {
            'project': project,
            'env': env,
            'update_date': update_date,
        }


class OverviewList(ListView):
    """Listing of all projects available.

    Extends :class:`django.views.generic.list.ListView`.

    If the user is not authenticated, then projects defined in
    :data:`SPHINXDOC_PROTECTED_PROJECTS` will not be listed.
    """
    queryset = Project.objects.all().order_by('name')
    template_name = 'sphinxdoc/project_list.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        qs = super(OverviewList, self).get_queryset()
        qs = [project for project in qs if project.is_allowed(self.request.user)]
        # Note: we are not actually returning a queryset, but a list. This has
        # some repercussions if there are dependencies elsewhere in the class
        # on this actually being a queryset.
        return qs

    def get_context_data(self, **kwargs):
        kwargs['base_template'] = getattr(settings, 'SPHINXDOC_BASE_TEMPLATE', 'base.html')
        context = super(OverviewList, self).get_context_data(**kwargs)
        return context


