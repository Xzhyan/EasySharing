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

@register.filter
def format_current_path(main_folder):
    if 'archives' in main_folder:
        return 'archives' + main_folder.split('archives', 1)[1]
    return main_folder