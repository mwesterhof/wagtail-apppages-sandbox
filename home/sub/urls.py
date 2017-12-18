from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from home.views import SubTestView


urlpatterns = [
    url(r'^subtest/', SubTestView.as_view(), name='subtest'),
]
