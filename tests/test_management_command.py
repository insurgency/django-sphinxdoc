# encoding: utf-8
from __future__ import print_function, unicode_literals

import pytest
from django.core.management import call_command
from .factories import ProjectFactory


__all__ = ['TestManagementCommand']


@pytest.mark.django_db
class TestManagementCommand(object):
    def assert_index_content_is_present(self, project):
        index = project.document_set.get(path='index')
        title = 'Sample Project'
        content = 'This is a sample project documentation for test purpouses.'
        assert title in index.body
        assert content in index.body

    @pytest.mark.django_db
    def test_updatedoc_build_specific_project(self):
        project = ProjectFactory(name='Sample Project', slug='sampleproject', path='tests/docs/')
        call_command('updatedoc', 'sampleproject', build=True)
        self.assert_index_content_is_present(project)

    @pytest.mark.django_db
    def test_updatedoc_build_all_projects(self):
        project = ProjectFactory(name='Sample Project', slug='sampleproject', path='tests/docs/')
        call_command('updatedoc', build=True, update_all=True)
        self.assert_index_content_is_present(project)
