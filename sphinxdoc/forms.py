# encoding: utf-8

from haystack.forms import SearchForm
from haystack.query import SearchQuerySet

from sphinxdoc.models import Project, Document


class ProjectSearchForm(SearchForm):
    def __init__(self, *args, **kwargs):
        slug = kwargs.pop('slug')
        project = Project.objects.get(slug=slug)
        kwargs['searchqueryset'] = SearchQuerySet().models(Document).filter(
                project=project.id)
        
        SearchForm.__init__(self, *args, **kwargs)
