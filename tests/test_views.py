# encoding: utf-8
from __future__ import print_function, unicode_literals

import pytest
from django.core.management import call_command
from django.conf import settings
from sphinxdoc.models import Project


__all__ = ['test_project_list',
           'test_doc_index',
           'test_default_base_template',
           'test_custom_base_template']


@pytest.fixture
def project():
    call_command('loaddata', 'built_sampleproject', verbosity=0)
    return Project.objects.get()


@pytest.mark.django_db
def test_project_list(client, project):
    response = client.get('/docs/')
    assert response.status_code == 200
    expected_project_list = [project]
    assert response.context['project_list'] == expected_project_list
    assert response.context['object_list'] == expected_project_list


@pytest.mark.django_db
def test_doc_index(client, project):
    response = client.get('/docs/sampleproject/')
    assert response.status_code == 200
    title = 'Sample Project'
    content = 'This is a sample project documentation for test purpouses.'
    body = response.content.decode('utf-8')
    assert title in body
    assert content in body


def assert_base_template_used(client, expected_term):
    """
    Make sure the project list uses the given base template.
    """
    response = client.get('/docs/')
    assert response.status_code == 200
    assert expected_term in response.content.decode('utf-8')


@pytest.mark.django_db
def test_default_base_template(client, project):
    assert_base_template_used(client, 'standard base template')


@pytest.mark.django_db
def test_custom_base_template(client, project):
    settings.SPHINXDOC_BASE_TEMPLATE = 'custom_base.html'
    assert_base_template_used(client, 'custom base template')
