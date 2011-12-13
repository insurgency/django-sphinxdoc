# encoding: utf-8
"""
Models for django-sphinxdoc.

"""
from django.db import models

from sphinxdoc.validators import validate_isdir


class Project(models.Model):
    """
    Represents a Sphinx project. Each ``Project`` has a name, a slug and a path
    to the root directory of a Sphinx project (where Sphinx’ ``conf.py``) is
    located).

    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,
            help_text=u'Used in the URL for the project. Must be unique.')
    path = models.CharField(max_length=255, validators=[validate_isdir],
            help_text=u'Directory that contains Sphinx’ <tt>conf.py</tt>.')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('doc-index', (), {'slug': self.slug})


class Document(models.Model):
    """
    Represents a JSON encoded Sphinx document. The attributes ``title`` and
    ``body`` dubicate the corresponding keys in ``content`` and are used for
    the Haystack search.

    """
    project = models.ForeignKey(Project)
    path = models.CharField(max_length=255)
    content = models.TextField()
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)

    def __unicode__(self):
        return self.path

    @models.permalink
    def get_absolute_url(self):
        return ('doc-detail', (), {
            'slug': self.project.slug,
            'path': self.path,
        })
