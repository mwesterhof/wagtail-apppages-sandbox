from __future__ import absolute_import, unicode_literals

from wagtail.wagtailcore.models import Page
from app_pages.models import AppPageMixin


class HomePage(AppPageMixin, Page):
    url_config = 'home.urls'
