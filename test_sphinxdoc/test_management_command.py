# encoding: utf-8

from __future__ import print_function, unicode_literals

from django.core.management import call_command
from django.test import TestCase
from nose.tools import assert_false, assert_in
from sphinxdoc.models import Project


__all__ = ['ManagementCommandTestCase']


class ManagementCommandTestCase(TestCase):
    fixtures = ['sampleproject']

    def setUp(self):
        self.project = Project.objects.get()
        assert_false(
            self.project.document_set.exists(),
            'The project shouldn\'t have any document before build.'
        )

    def check_index_content(self):
        index = self.project.document_set.get(path='index')
        assert_in('Sample Project', index.body)
        assert_in('This is a sample project documentation for test purpouses.', index.body)

    def test_updatedoc_build_specific_project(self):
        call_command('updatedoc', 'sampleproject', build=True)
        self.check_index_content()

    def test_updatedoc_build_all_projects(self):
        call_command('updatedoc', build=True, update_all=True)
        self.check_index_content()
