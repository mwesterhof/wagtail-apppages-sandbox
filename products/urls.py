from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import ProductDetail, ProductList


urlpatterns = [
    url(r'^$', ProductList.as_view(), name='product-list'),
    url(r'^(?P<pk>\d+)/$', ProductDetail.as_view(), name='product-detail'),
]
