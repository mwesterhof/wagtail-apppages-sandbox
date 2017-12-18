from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from home.views import SubSubTestView


urlpatterns = [
    url(r'^subsubtest/', SubSubTestView.as_view()),
]
