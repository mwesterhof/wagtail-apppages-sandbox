from django.template import Library

register = Library()


@register.simple_tag(takes_context=True)
def page_url(context, name, *args, **kwargs):
    return context['view'].kwargs['parent_page'].reverse(name, *args)
