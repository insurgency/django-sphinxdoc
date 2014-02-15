"""
Search indexes for Haystack.

"""
from haystack import indexes

from sphinxdoc.models import Document


class DocumentIndex(indexes.SearchIndex, indexes.Indexable):
    """Index for :class:`~sphinxdoc.models.Document`.

    """
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    project = indexes.IntegerField(model_attr='project_id')

    def get_model(self):
        return Document
