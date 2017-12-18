from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from home.views import SubTestView
from home.sub import urls_sub as subsub_urls


urlpatterns = [
    url(r'^subtest/$', SubTestView.as_view(), name='subtest'),
    url(r'^subsubtest/', include(subsub_urls)),
]
