from django.conf.urls import url, include


urlpatterns = [
    url(r'^docs/', include('sphinxdoc.urls')),
]
