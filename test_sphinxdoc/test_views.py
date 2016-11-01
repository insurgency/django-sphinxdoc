# encoding: utf-8

from __future__ import print_function, unicode_literals

from django.test import TestCase, override_settings
from nose.tools import assert_equals, assert_in
from sphinxdoc.models import Project


__all__ = ['ViewsTestCase']


class ViewsTestCase(TestCase):
    fixtures = ['built_sampleproject']

    def setUp(self):
        self.project = Project.objects.get()

    def test_project_list(self):
        response = self.client.get('/docs/')
        assert_equals(response.status_code, 200)
        expected_project_list = [self.project]
        assert_equals(response.context['project_list'], expected_project_list)
        assert_equals(response.context['object_list'], expected_project_list)

    def test_doc_index(self):
        response = self.client.get('/docs/sampleproject/')
        assert_equals(response.status_code, 200)
        content = response.content.decode('utf-8')
        assert_in('Sample Project', content)
        assert_in('This is a sample project documentation for test purpouses.', content)

    def test_base_template_default(self):
        response = self.client.get('/docs/')
        assert_equals(response.status_code, 200)
        base_template = response.templates[-1]
        assert_equals(base_template.name, 'base.html')

    @override_settings(SPHINXDOC_BASE_TEMPLATE='custom_base.html')
    def test_custom_base_template(self):
        response = self.client.get('/docs/sampleproject/')
        assert_equals(response.status_code, 200)
        base_template = response.templates[-1]
        assert_equals(base_template.name, 'custom_base.html')
