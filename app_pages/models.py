'''
TODO:
    * allow anonymous urls
    * ensure unique method names

'''
from importlib import import_module

from django.urls import reverse as django_reverse
from django.urls.resolvers import RegexURLResolver
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route


def _concat_regex(left, right):
    joined = left.strip(r'$') + right.strip(r'^')
    return r'^' + joined.lstrip(r'^')


def _attach_route(page, pattern, regex):
    def create_method(pattern):
        def method(self, request, *args, **kwargs):
            kwargs['parent_page'] = self
            return pattern.callback(request, *args, **kwargs)

        method.__name__ = pattern.name
        return route(regex)(method)

    setattr(
        page, pattern.name.replace('-', '_'), create_method(pattern))


def _attach_routes(page, patterns, prefix_path=''):
    for entry in patterns:

        regex = prefix_path.strip(r'$') + entry.regex.pattern.strip(r'^')
        regex = _concat_regex(prefix_path, entry.regex.pattern)

        if isinstance(entry, RegexURLResolver):  # entry is an include, recurse
            _attach_routes(page, entry.url_patterns, regex)
        else:
            _attach_route(page, entry, regex)


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

        _attach_routes(cls, url_config.urlpatterns)

        return RoutablePageMixin.__new__(cls)
