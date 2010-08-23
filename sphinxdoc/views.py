# encoding: utf-8

import datetime
import os.path

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson as json
from django.views import static

from sphinxdoc.models import Project, Document


def documentation(request, slug, path):
    app = get_object_or_404(Project, slug=slug)
    path = path.strip('/')
    page_name = os.path.basename(path)
    
    try:
        doc = Document.objects.get(project=project, 
                path='%s/index.fjson' % path)
    except ObjectDoesNotExist:
        doc = get_object_or_404(Document, project=project, 
                path='%s.fjson' % path)

    templates = (
        'sphinxdoc/%s.html' % page_name,
        'sphinxdoc/documentation.html',
    )
    
    data = {
        'project': project,
        'doc': json.load(open(path, 'rb')),
        'env': json.load(open(
                os.path.join(project.path, 'globalcontext.json'), 'rb')),
        'version': project.name,
        'docurl': self.get_absolute_url(),
        'update_date':  datetime.datetime.fromtimestamp(
                os.path.getmtime(os.path.join(project.path, 'last_build'))),
        'home': project.get_absolute_url(),
        'search': urlresolvers.reverse('doc-search', kwargs={'slug':slug}),
        'redirect_from': request.GET.get('from', None),
    
    }
    if 'title' not in data['doc']:
        data['doc']['title'] = SPECIAL_TITLES[page_name]
        
    return render_to_response(templates, data,
            context_instance=RequestContext(request))

def search(request, slug):
    from django.http import HttpResponse
    return HttpResponse('Not yet implemented.')
    
def objects_inventory(request, slug):
    project = get_object_or_404(Project, slug=slug)
    response = static.serve(
        request, 
        document_root = project.path,
        path = "objects.inv",
    )
    response['Content-Type'] = "text/plain"
    return response

def images(request, slug, path):
    project = get_object_or_404(Project, slug=slug)
    return static.serve(
        request, 
        document_root = os.path.join(project.path, '_images'),
        path = path,
    )
    
def source(request, slug, path):
    project = get_object_or_404(Project, slug=slug)
    return static.serve(
        request,
        document_root = os.path.join(project.path, '_sources'),
        path = path,
    )
