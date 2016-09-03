from django import template

register = template.Library()

@register.filter(name = 'partition_url')
def partition_url(value):
    return value.partition('-')[2]