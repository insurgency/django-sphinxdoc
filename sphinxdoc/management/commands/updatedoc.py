# encoding: utf-8

import json
import optparse
import os
import os.path
import subprocess

from django.core.management.base import BaseCommand, CommandError

from sphinxdoc.models import Project, Document


BUILDDIR = '_build'
EXTENSION = '.fjson'
SPECIAL_TITLES = {
    'genindex': 'General Index',
    'modindex': 'Module Index',
    'search': 'Search',
}


class Command(BaseCommand):
    args = '<project_slug project_slug ...>'
    help = ('Updates the documentation and the search index for the specified '
            'projects.')    
    option_list = BaseCommand.option_list + (
        optparse.make_option('-b', '--build',
            action='store_true',
            dest='build',
            default=False,
            help='Run "sphinx-build" for each project before updating it.'),
        optparse.make_option('--virtualenv',
            dest='virtualenv',
            default='',
            help='Use this virtualenv to build project docs.'
        )
    )


    def handle(self, *args, **options):
        build = options['build']
        virtualenv = options['virtualenv']
        
        for slug in args:
            try:
                project = Project.objects.get(slug=slug)
            except Project.DoesNotExist:
                raise CommandError('Project "%s" does not exist' % slug)

            if build:
                print 'Running "sphinx--build" for "%s" ...' % slug
                self.build(project, virtualenv)

            print 'Deleting old entries from database ...'
            self.delete_documents(project)

            print 'Importing JSON files for "%s" ...' % slug
            self.import_files(project)
            
            print 'Updating search index for "%s" ...' % slug
            
            print 'Done'
            
    def build(self, project, virtualenv):
        cmd = 'sphinx-build'
        if virtualenv:
            cmd = os.path.join(virtualenv, cmd)
        cmd = [
            cmd,
            '-b',
            'json',
            '-d',
            os.path.join(project.path, BUILDDIR, 'doctrees'),
            project.path,
            os.path.join(project.path, BUILDDIR, 'json'),
        ]
        subprocess.call(cmd)
        
    def delete_documents(self, project):
        Document.objects.filter(project=project).delete()
        
    def import_files(self, project):
        path = os.path.join(project.path, BUILDDIR, 'json')
        for dirpath, dirnames, filenames in os.walk(path):
            for name in filter(lambda x: x.endswith(EXTENSION), filenames):
                # Full path to the json file
                filepath = os.path.join(dirpath, name)
                
                # Get path relative to the build dir w/o file extension
                relpath = os.path.relpath(filepath, path)[:-len(EXTENSION)]
                
                # Some files have no title or body attribute
                doc = json.load(open(filepath, 'rb'))
                if 'title' not in doc:
                    page_name = os.path.basename(relpath)
                    doc['title'] = SPECIAL_TITLES[page_name]
                if 'body' not in doc:
                    doc['body'] = ''
                
                # Finally create the Document
                d = Document(
                    project=project,
                    path=relpath,
                    content=json.dumps(doc),
                    title=doc['title'],
                    body=doc['body']
                )
                d.full_clean()
                d.save()
