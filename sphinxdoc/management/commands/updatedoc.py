import optparse
import os.path
import subprocess

from django.core.management.base import BaseCommand, CommandError

from sphinxdoc.models import Project, Document


BUILDDIR = '_build'


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

            print 'Importing JSON files for "%s" ...' % slug
            
            print 'Updating search index for "%s" ...' % slug
            
            print 'Done'
