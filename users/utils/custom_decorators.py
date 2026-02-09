from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def check_permission(redirect_to):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_admin:
                messages.error(request, "Sem autorização!")
                return redirect(redirect_to)
            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator