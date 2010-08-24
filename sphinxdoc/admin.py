# encoding: utf-8
'''
Admin interface for the sphinxdoc app.
'''

from django.contrib import admin

from sphinxdoc.models import Project, Document


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'path',)
    prepopulated_fields = {'slug': ('name',)}
    

class DocumentAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(Project, ProjectAdmin)
admin.site.register(Document, DocumentAdmin)
