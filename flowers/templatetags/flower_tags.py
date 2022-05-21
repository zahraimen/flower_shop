from django import template
import re

register = template.Library()


@register.filter
def is_english(value):
    reg = re.compile(r'[a-zA-Z]')
    if reg.match(value):
        return value.
    else:
        print("It is not an alphabet")