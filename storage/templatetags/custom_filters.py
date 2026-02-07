from django import template

register = template.Library()

@register.filter
def format_size(value):
    size = float(value)
    for unit in ['KB', 'MB', 'GB', 'TB']:
        size /= 1024
        if size < 1024:
            return f"{size:.2f} {unit}"
    return f"{size:.2f} PB"