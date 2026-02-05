from django import template

register = template.Library()

@register.filter
def format_size(value):
    if value < 1.0:
        value = f'{value} KBs'
        return value

    elif value > 1.0:
        value = f'{value} MBs'
        return value

    elif value > 1024:
        value = f'{value} GBs'
        return value