from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            # print(requesst.user.get_user_permissions)
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            # print(group)
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.warning(request, 'You don\'t have permission to acces this page!', extra_tags='permissions')
                return redirect(request.META.get('HTTP_REFERER'))

            
        
        return wrapper_func
    return decorator