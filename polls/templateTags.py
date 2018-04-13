#if we need another template tag, information here: https://stackoverflow.com/questions/40686201/django-1-10-1-my-templatetag-is-not-a-registered-tag-library-must-be-one-of
from django import template

register = template.Library()

@register.tag('at_index')
def at_index(data, index):
    return data[index]