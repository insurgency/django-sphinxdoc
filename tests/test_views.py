# encoding: utf-8
from __future__ import print_function, unicode_literals

import pytest
from django.core.management import call_command
from django.conf import settings
from sphinxdoc.models import Project
from .factories import ProjectFactory


__all__ = ['TestViewsContent', 'TestBaseTemplate']


@pytest.fixture
def project():
    call_command('loaddata', 'built_sampleproject', verbosity=0)
    return Project.objects.get()


@pytest.mark.django_db
class TestViewsContent(object):
    def test_project_list(self, client, project):
        response = client.get('/docs/')
        assert response.status_code == 200
        expected_project_list = [project]
        assert response.context['project_list'] == expected_project_list
        assert response.context['object_list'] == expected_project_list

    def test_doc_index(self, client, project):
        response = client.get('/docs/sampleproject/')
        assert response.status_code == 200
        title = 'Sample Project'
        content = 'This is a sample project documentation for test purpouses.'
        body = response.content.decode('utf-8')
        assert title in body
        assert content in body


@pytest.mark.django_db
class TestBaseTemplate(object):
    def assert_base_template_used(self, client, expected_term):
        """
        Make sure the project list and doc index uses the given base template.
        """
        responses = [client.get('/docs/'),
                     client.get('/docs/sampleproject/')]
        for response in responses:
            assert response.status_code == 200
            assert expected_term in response.content.decode('utf-8')

    def test_base_template_default(self, client, project):
        self.assert_base_template_used(client, 'standard base template')

    def test_custom_base_template(self, client, project):
        settings.SPHINXDOC_BASE_TEMPLATE = 'custom_base.html'
        self.assert_base_template_used(client, 'custom base template')
