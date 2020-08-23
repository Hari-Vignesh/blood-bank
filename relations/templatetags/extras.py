from django import template

register = template.Library()

@register.filter(name="capitalize")
def capitalize(word):
    return word.upper()