from functools import wraps

from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ImproperlyConfigured
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.utils.decorators import available_attrs

from sphinxdoc.models import Project


def user_allowed_for_project(view_func):
    """
    Check that the user is allowed for the project.

    If the user is not allowed, the view will be redirected to the standard
    login page.
    """
    @wraps(view_func, assigned=available_attrs(view_func))
    def _wrapped_view(request, *args, **kwargs):
        try:
            slug = kwargs['slug']
        except IndexError:
            raise ImproperlyConfigured
        project = get_object_or_404(Project, slug=slug)
        if project.is_allowed(request.user):
            return view_func(request, *args, **kwargs)
        if request.user.is_authenticated():
            raise PermissionDenied
        path = request.build_absolute_uri()
        return redirect_to_login(path)
    return _wrapped_view


