from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from home.views import AppTestView, ParamTestView
from home.sub import urls as sub_urls


urlpatterns = [
    url(r'^$', AppTestView.as_view()),
    url(r'^foo/bar/baz/$', AppTestView.as_view()),
    url(r'^paramtest/(?P<test>[^/]+)/$', ParamTestView.as_view()),
    url(r'^sub/', include(sub_urls)),
]
