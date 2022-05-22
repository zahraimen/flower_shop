from django import template
import re

register = template.Library()


@register.filter
def is_english(value):
    reg = re.compile(r'[a-z]')
    if reg.match(value):
        return value.title()
    else:
        return value
