from django import template

register = template.Library()

@register.filter
def first_word(value):
    """
    Returns the first word of the given string.
    """
    return value.split()[0] if value else ''
