# encoding: utf-8
'''
Admin interface for the sphinxdoc app.
'''

from django.contrib import admin

from sphinxdoc.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'path',)
    prepopulated_fields = {'slug': ('name',)}
    

admin.site.register(Project, ProjectAdmin)
