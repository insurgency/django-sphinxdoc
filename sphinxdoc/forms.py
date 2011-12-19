# encoding: utf-8
"""
Forms for the sphinxdoc app.

"""
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet

from sphinxdoc.models import Project, Document


class ProjectSearchForm(SearchForm):
    """
    Custom search form for Haystack.

    It narrows the search query set to instances of
    :class:`~sphinxdoc.models.Document` that belong to the current
    :class:`~sphinxdoc.models.Project`.

    """
    def __init__(self, *args, **kwargs):
        slug = kwargs.pop('slug')
        project = Project.objects.get(slug=slug)
        kwargs['searchqueryset'] = (kwargs.get('searchqueryset') or
                SearchQuerySet()).models(Document).filter(project=project.id)

        SearchForm.__init__(self, *args, **kwargs)
