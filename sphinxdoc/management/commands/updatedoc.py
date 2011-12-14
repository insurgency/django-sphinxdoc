# encoding: utf-8
"""
Management command for updading the documentation of one or more projects.

"""
import json
import optparse
import os
import os.path
import subprocess

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from sphinxdoc.models import Project, Document


BUILDDIR = '_build'
EXTENSION = '.fjson'
SPECIAL_TITLES = {
    'genindex': 'General Index',
    'py-modindex': 'Module Index',
    'np-modindex': 'Module Index',
    'search': 'Search',
}


class Command(BaseCommand):
    """
    Update (and optionally build) the *Sphinx* documentation for one ore more
    projects.

    You need to pass the slug of at least one project. If you pass the optional
    parameter ``-b``, the command ``sphinx-build`` will be run for each project
    before their files are read. If your project(s) are located in a different
    *virtualenv* than your django site, you can provide a path to its
    interpreter with ``--virtualenv path/to/env/bin/``

    """
    args = '[-b [--virtualenv <path/to/bin/>]] <project_slug project_slug ...>'
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
            help='Use this virtualenv to build project docs.',
        )
    )

    def handle(self, *args, **options):
        """
        Updates (and optionally builds) the documenation for all projects in
        ``args``.

        """
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
            self.update_haystack()

            print 'Done'

    def build(self, project, virtualenv=''):
        """
        Runs ``sphinx-build`` for ``project``. You can also specify a path to
        the bin-directory of a ``virtualenv``, if your project requires it.

        """
        cmd = 'sphinx-build'
        if virtualenv:
            cmd = os.path.expanduser(os.path.join(virtualenv, cmd))
        cmd = [
            cmd,
            '-b',
            'json',
            '-d',
            os.path.join(project.path, BUILDDIR, 'doctrees'),
            project.path,
            os.path.join(project.path, BUILDDIR, 'json'),
        ]
        print 'Executing %s' % ' '.join(cmd)
        subprocess.call(cmd)

    def delete_documents(self, project):
        """Deletes all documents for ``project``."""
        Document.objects.filter(project=project).delete()

    def import_files(self, project):
        """
        Creates a :class:`~sphinxdoc.models.Document` instance for each JSON
        file of ``project``.
        """
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
                    body=doc['body'],
                )
                d.full_clean()
                d.save()

    def update_haystack(self):
        """Updates Haystack’s search index."""
        call_command('rebuild_index', interactive=False)
