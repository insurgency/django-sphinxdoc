# encoding: utf-8
"""
Search indexes for Haystack.

"""
from haystack import indexes, site

from sphinxdoc.models import Document


class DocumentIndex(indexes.SearchIndex):
    """
    Index for :class:`~sphinxdoc.models.Document`.

    """
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    project = indexes.IntegerField(model_attr='project_id')

    def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Document.objects.all()


site.register(Document, DocumentIndex)
