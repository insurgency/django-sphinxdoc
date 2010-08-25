# encoding: utf-8

from haystack import indexes, site

from sphinxdoc.models import Document


class DocumentIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    
    def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Document.objects.all()


site.register(Document, DocumentIndex)
