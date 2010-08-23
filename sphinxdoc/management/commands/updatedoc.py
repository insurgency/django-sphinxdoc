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
        
    def import_files(self, project):
        path = os.path.join(project.path, BUILDDIR, 'json')
        for dirpath, dirnames, filenames in os.walk(path):
            for name in filter(lambda x: x.endswith(EXTENSION), filenames):
                path = os.path.join(dirpath, name)
                doc = json.load(open(path, 'r'))
