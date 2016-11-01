# encoding: utf-8

from __future__ import print_function, unicode_literals

from django.core.management import call_command
from django.test import TestCase
from nose.tools import assert_false, assert_equals
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
