from django import template
from django.template.defaultfilters import stringfilter

import markdown as md

register = template.Library()


@register.filter
@stringfilter
def markdown_to_html(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code', 'tables', 'toc'])

