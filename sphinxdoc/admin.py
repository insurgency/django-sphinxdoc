"""
Admin interface for the sphinxdoc app.

"""
from django.contrib import admin

from sphinxdoc.models import Project, Document


class ProjectAdmin(admin.ModelAdmin):
    """Admin interface for :class:`~sphinxdoc.models.Project`."""
    list_display = ('name', 'path',)
    prepopulated_fields = {'slug': ('name',)}


class DocumentAdmin(admin.ModelAdmin):
    """Admin interface for :class:`~sphinxdoc.models.Document`.

    Normally, you shouldn't need this, since you create new documents via
    the management command.

    """
    list_display = ('path', 'title', 'project',)
    list_filter = ('project', )


admin.site.register(Project, ProjectAdmin)
admin.site.register(Document, DocumentAdmin)
