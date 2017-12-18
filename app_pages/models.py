from importlib import import_module

from django.urls import reverse as django_reverse
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route


def _attach_route(page, pattern):
    def create_method(pattern):
        def method(self, request, *args, **kwargs):
            kwargs['parent_page'] = self
            return pattern.callback(request, *args, **kwargs)

        method.__name__ = pattern.name
        return route(pattern.regex.pattern)(method)

    setattr(
        page, pattern.name.replace('-', '_'), create_method(pattern))


class AppPageMixin(RoutablePageMixin):
    @property
    def url_config(self):
        raise NotImplementedError('url_config')

    def reverse(self, name, *args, **kwargs):
        sub_url = django_reverse(
            name, urlconf=self.url_config, *args, **kwargs)
        return self.url + sub_url.lstrip('/')

    def __new__(cls, *args, **kwargs):
        url_config = import_module(cls.url_config)

        for pattern in url_config.urlpatterns:
            _attach_route(cls, pattern)

        return RoutablePageMixin.__new__(cls)
